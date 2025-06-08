import os
import requests
from tqdm import tqdm
from typing import List


def bruteforce(url: str, wordlist: List[str]) -> List[str]:
    """Discover hidden directories/files."""
    found = []
    for word in tqdm(wordlist, desc="Dir Bruteforce"):
        target = os.path.join(url, word)
        try:
            resp = requests.get(target, timeout=5)
            if resp.status_code < 400:
                found.append(target)
        except Exception:
            continue
    return found
