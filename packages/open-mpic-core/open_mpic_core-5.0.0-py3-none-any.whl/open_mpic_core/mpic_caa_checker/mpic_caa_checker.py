import time
from typing import Final
import dns.resolver
import dns.asyncresolver
from dns.name import Name
from dns.rrset import RRset

from open_mpic_core import CaaCheckRequest, CaaCheckResponse, CaaCheckResponseDetails
from open_mpic_core import MpicValidationError, ErrorMessages
from open_mpic_core import DomainEncoder
from open_mpic_core import get_logger

ISSUE_TAG: Final[str] = "issue"
ISSUEWILD_TAG: Final[str] = "issuewild"
# to accommodate email and phone based DCV that gets contact info from CAA records
CONTACTEMAIL_TAG: Final[str] = "contactemail"
CONTACTPHONE_TAG: Final[str] = "contactphone"


logger = get_logger(__name__)


class MpicCaaLookupException(Exception):  # This is a python exception type used for raise statements.
    pass


class MpicCaaChecker:
    def __init__(self, default_caa_domain_list: list[str], log_level: int = None):
        self.default_caa_domain_list = default_caa_domain_list

        self.logger = logger.getChild(self.__class__.__name__)
        if log_level is not None:
            self.logger.setLevel(log_level)

    @staticmethod
    def does_value_list_permit_issuance(value_list: list, caa_domains):
        for value in value_list:
            # We currently do not have any parsing for CAA extensions, so we'll never accept a value with an extension.
            if ";" in value:
                continue
            # One of the CAA records in this set was an exact match on a CAA domain
            value_no_whitespace = value.strip()
            if value_no_whitespace in caa_domains:
                return True
        # If nothing matched, we cannot issue.
        return False

    @staticmethod
    async def find_caa_records_and_domain(caa_request) -> tuple[RRset, Name]:
        rrset = None
        domain = dns.name.from_text(caa_request.domain_or_ip_target)

        while domain != dns.name.root:
            try:
                lookup = await dns.asyncresolver.resolve(domain, dns.rdatatype.CAA)
                rrset = lookup.rrset
                break
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                domain = domain.parent()
            except Exception as e:
                print(f"Exception during CAA lookup: {e}")
                raise MpicCaaLookupException from Exception(e)

        return rrset, domain

    @staticmethod
    def is_valid_for_issuance(caa_domains, is_wc_domain, rrset):
        issue_tags = []
        issue_wild_tags = []
        has_unknown_critical_flags = False

        # Note: a record with critical flag and 'issue' tag will be considered valid for issuance
        for resource_record in rrset:
            tag = resource_record.tag.decode("utf-8")
            tag_lower = tag.lower()
            val = resource_record.value.decode("utf-8")
            if tag_lower == ISSUE_TAG:
                issue_tags.append(val)
            elif tag_lower == ISSUEWILD_TAG:
                issue_wild_tags.append(val)
            elif (
                tag_lower != CONTACTEMAIL_TAG and tag_lower != CONTACTPHONE_TAG and resource_record.flags & 0b10000000
            ):  # bitwise-and to check if flags are 128 (the critical flag)
                has_unknown_critical_flags = True

        if has_unknown_critical_flags:
            valid_for_issuance = False
        else:
            if is_wc_domain and len(issue_wild_tags) > 0:
                valid_for_issuance = MpicCaaChecker.does_value_list_permit_issuance(issue_wild_tags, caa_domains)
            elif len(issue_tags) > 0:
                valid_for_issuance = MpicCaaChecker.does_value_list_permit_issuance(issue_tags, caa_domains)
            else:
                # We had no unknown critical tags, and we found no issue tags. Issuance can proceed.
                valid_for_issuance = True
        return valid_for_issuance

    async def check_caa(self, caa_request: CaaCheckRequest) -> CaaCheckResponse:
        # noinspection PyUnresolvedReferences
        self.logger.trace(f"Checking CAA for {caa_request.domain_or_ip_target}")

        # Assume the default system configured validation targets and override if sent in the API call.
        caa_domains = self.default_caa_domain_list
        is_wc_domain = False
        if caa_request.caa_check_parameters:
            if caa_request.caa_check_parameters.caa_domains:
                caa_domains = caa_request.caa_check_parameters.caa_domains

            # Use the domain name to determine if it is a wildcard domain
            # check if domain or ip target has an asterisk as its lowest (first) label (e.g. *.example.com)
            if caa_request.domain_or_ip_target.startswith("*."):
                is_wc_domain = True

        caa_lookup_error = False
        caa_found = False
        domain = None
        rrset = None

        caa_check_response = CaaCheckResponse(
            check_passed=False,
            errors=None,
            details=CaaCheckResponseDetails(caa_record_present=None),
            timestamp_ns=None,
        )

        # encode domain if needed
        caa_request.domain_or_ip_target = DomainEncoder.prepare_target_for_lookup(caa_request.domain_or_ip_target)

        try:
            # noinspection PyUnresolvedReferences
            async with self.logger.trace_timing(f"CAA lookup for target {caa_request.domain_or_ip_target}"):
                rrset, domain = await MpicCaaChecker.find_caa_records_and_domain(caa_request)
            caa_found = rrset is not None
        except MpicCaaLookupException:
            caa_lookup_error = True

        if caa_lookup_error:
            caa_check_response.errors = [
                MpicValidationError(
                    error_type=ErrorMessages.CAA_LOOKUP_ERROR.key, error_message=ErrorMessages.CAA_LOOKUP_ERROR.message
                )
            ]
            caa_check_response.details.found_at = None
            caa_check_response.details.records_seen = None
        elif not caa_found:  # if domain has no CAA records: valid for issuance
            caa_check_response.check_passed = True
            caa_check_response.details.caa_record_present = False
            caa_check_response.details.found_at = None
            caa_check_response.details.records_seen = None
        else:
            valid_for_issuance = MpicCaaChecker.is_valid_for_issuance(caa_domains, is_wc_domain, rrset)
            caa_check_response.check_passed = valid_for_issuance
            caa_check_response.details.caa_record_present = True
            caa_check_response.details.found_at = domain.to_text(omit_final_dot=True)
            caa_check_response.details.records_seen = [record_data.to_text() for record_data in rrset]
        caa_check_response.timestamp_ns = time.time_ns()

        # noinspection PyUnresolvedReferences
        self.logger.trace(f"Completed CAA for {caa_request.domain_or_ip_target}")
        return caa_check_response
