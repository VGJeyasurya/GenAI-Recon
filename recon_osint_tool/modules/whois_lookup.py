import whois


def lookup(domain: str) -> str:
    """Return WHOIS info for a domain as string."""
    try:
        return whois.whois(domain).text
    except Exception as e:
        return str(e)
