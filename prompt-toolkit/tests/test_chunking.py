from prompt_toolkit_lite.chunking import chunk_text
from prompt_toolkit_lite import estimate_tokens
def test_chunks_fit():
    c = chunk_text("lorem ipsum " * 200, 20, overlap=4)
    assert len(c) > 1 and all(estimate_tokens(x) <= 20 for x in c)
