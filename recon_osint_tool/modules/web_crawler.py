import requests
from bs4 import BeautifulSoup
from typing import List
from tqdm import tqdm


def crawl(url: str, limit: int = 10) -> List[str]:
    """Simple web crawler that returns discovered links."""
    visited = []
    to_visit = [url]
    while to_visit and len(visited) < limit:
        current = to_visit.pop(0)
        if current in visited:
            continue
        try:
            resp = requests.get(current, timeout=5)
            soup = BeautifulSoup(resp.text, "html.parser")
            visited.append(current)
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('http') and href not in visited:
                    to_visit.append(href)
        except Exception:
            continue
    return visited
