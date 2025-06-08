import os
from typing import List

import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("TOGETHER_API_KEY")
openai.api_key = OPENAI_API_KEY


def generate_email_patterns(names: List[str], domain: str) -> str:
    """Generate probable email patterns using Together.ai API."""
    prompt = (
        "Given these names: "
        + ", ".join(names)
        + f" and domain: {domain}, generate possible corporate email formats."
    )
    try:
        response = openai.Completion.create(
            model="togethercomputer/llama-2-70b-chat",
            prompt=prompt,
            max_tokens=150,
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        return str(e)
