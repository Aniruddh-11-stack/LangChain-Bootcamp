from prompt_toolkit_lite.fewshot import few_shot
def test_few_shot():
    out = few_shot("Classify.", [{"text": "great", "label": "pos"}], "Text: {text}\nLabel: {label}", {"text": "bad"})
    assert "Text: great\nLabel: pos" in out and out.endswith("Text: bad\nLabel: {label}")
