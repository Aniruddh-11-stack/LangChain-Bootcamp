# llm-prompt-toolkit

Lightweight Python utilities for LLM prompt work: templates with variable validation, partial filling, and quick token-budget estimates.

```python
from prompt_toolkit_lite import PromptTemplate, truncate_to_budget
t = PromptTemplate("Summarise for {audience}:\n{doc}")
print(t.render(audience="execs", doc=truncate_to_budget(long_text, 500)))
```

Run tests: `pytest`
