import re
from typing import List


EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"


def extract_emails(text: str) -> List[str]:
    """Extract emails from given text."""
    return re.findall(EMAIL_REGEX, text)
