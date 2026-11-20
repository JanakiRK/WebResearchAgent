
import re


def summarise_text(text: str, max_sentences: int = 5) -> str:
    """
    Create a simple summary by extracting the first few sentences.
    """

    if not isinstance(text, str) or not text.strip():
        raise ValueError("Text cannot be empty.")

    if not isinstance(max_sentences, int) or isinstance(max_sentences, bool):
        raise ValueError("max_sentences must be an integer.")

    if max_sentences < 1:
        raise ValueError("max_sentences must be at least 1.")

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    summary = " ".join(sentences[:max_sentences])

    return summary
