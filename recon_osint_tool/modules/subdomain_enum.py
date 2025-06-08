import dns.resolver
from typing import List
from tqdm import tqdm


def enumerate_subdomains(domain: str, subdomains: List[str]) -> List[str]:
    """Simple DNS brute-force to enumerate subdomains."""
    found = []
    resolver = dns.resolver.Resolver()
    for sub in tqdm(subdomains, desc="Subdomain Enum"):
        try:
            full_domain = f"{sub}.{domain}"
            resolver.resolve(full_domain, 'A')
            found.append(full_domain)
        except Exception:
            continue
    return found
