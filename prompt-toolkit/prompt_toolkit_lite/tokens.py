import math


def estimate_tokens(text: str) -> int:
    """Rough token estimate (~4 chars per token for English)."""
    return math.ceil(len(text) / 4) if text else 0


def truncate_to_budget(text: str, max_tokens: int) -> str:
    """Truncate text on a word boundary to fit an approximate token budget."""
    if estimate_tokens(text) <= max_tokens:
        return text
    cut = text[: max_tokens * 4]
    return cut.rsplit(" ", 1)[0] if " " in cut else cut
