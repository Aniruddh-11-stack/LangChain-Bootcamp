import pytest
from prompt_toolkit_lite.chat import ChatPrompt
def test_chat():
    m = ChatPrompt().system("s").user("u").to_list()
    assert m == [{"role": "system", "content": "s"}, {"role": "user", "content": "u"}]
def test_bad_role():
    with pytest.raises(ValueError): ChatPrompt().add("tool", "x")
