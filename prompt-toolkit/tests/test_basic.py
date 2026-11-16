import pytest
from prompt_toolkit_lite import PromptTemplate, estimate_tokens, truncate_to_budget


def test_render():
    t = PromptTemplate("Hi {name}, summarise {doc}")
    assert t.variables == ["doc", "name"]
    assert t.render(name="A", doc="x") == "Hi A, summarise x"


def test_missing():
    with pytest.raises(KeyError):
        PromptTemplate("{a}").render()


def test_partial():
    t = PromptTemplate("{a} and {b}").partial(a="1")
    assert t.variables == ["b"]


def test_tokens():
    assert estimate_tokens("") == 0
    assert estimate_tokens("abcd") == 1
    assert estimate_tokens(truncate_to_budget("word " * 100, 10)) <= 10
