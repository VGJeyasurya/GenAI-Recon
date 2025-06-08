import dns.resolver
from typing import Dict, List


RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]


def get_dns_records(domain: str) -> Dict[str, List[str]]:
    """Retrieve various DNS records for a domain."""
    records = {}
    resolver = dns.resolver.Resolver()
    for rtype in RECORD_TYPES:
        try:
            answers = resolver.resolve(domain, rtype)
            records[rtype] = [a.to_text() for a in answers]
        except Exception:
            records[rtype] = []
    return records
