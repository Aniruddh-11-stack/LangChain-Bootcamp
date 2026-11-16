from .tokens import estimate_tokens


def chunk_text(text: str, max_tokens: int, overlap: int = 0) -> list[str]:
    """Split text into word-based chunks that fit an approximate token budget."""
    if overlap >= max_tokens:
        raise ValueError("overlap must be smaller than max_tokens")
    words, chunks, cur = text.split(), [], []
    for w in words:
        if cur and estimate_tokens(" ".join(cur + [w])) > max_tokens:
            chunks.append(" ".join(cur))
            keep = []
            for x in reversed(cur):
                if estimate_tokens(" ".join([x] + keep)) > overlap: break
                keep.insert(0, x)
            cur = keep if overlap else []
        cur.append(w)
    if cur: chunks.append(" ".join(cur))
    return chunks
