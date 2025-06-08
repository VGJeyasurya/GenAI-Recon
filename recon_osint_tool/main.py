import os
import argparse
from .modules import (
    subdomain_enum,
    port_scanner,
    email_harvester,
    whois_lookup,
    dns_enum,
    web_crawler,
    directory_bruteforcer,
)


def parse_args():
    parser = argparse.ArgumentParser(description="Reconnaissance Framework")
    parser.add_argument("target", help="Target domain or IP")
    parser.add_argument("--wordlist", help="Wordlist for bruteforcing")
    return parser.parse_args()


def main():
    args = parse_args()
    domain = args.target
    print("WHOIS Lookup:")
    print(whois_lookup.lookup(domain))

    print("DNS Records:")
    print(dns_enum.get_dns_records(domain))

    wordlist = ["admin", "login", "test"]
    if args.wordlist and os.path.exists(args.wordlist):
        with open(args.wordlist) as f:
            wordlist = [line.strip() for line in f]

    print("Directory Bruteforce:")
    print(directory_bruteforcer.bruteforce(f"http://{domain}", wordlist))

    print("Subdomain Enumeration:")
    subs = ["www", "mail", "ftp"]
    print(subdomain_enum.enumerate_subdomains(domain, subs))

    print("Port Scan:")
    ports = [80, 443, 22]
    print(port_scanner.scan_ports(domain, ports))

    print("Web Crawl:")
    print(web_crawler.crawl(f"http://{domain}"))


if __name__ == "__main__":
    main()
