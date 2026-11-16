import re
from string import Formatter


class PromptTemplate:
    """A prompt template with {named} placeholders and validation."""

    def __init__(self, template: str):
        self.template = template
        self.variables = sorted(
            {f for _, f, _, _ in Formatter().parse(template) if f}
        )

    def render(self, **kwargs) -> str:
        missing = [v for v in self.variables if v not in kwargs]
        if missing:
            raise KeyError(f"Missing variables: {', '.join(missing)}")
        return self.template.format(**kwargs)

    def partial(self, **kwargs) -> "PromptTemplate":
        text = self.template
        for k, v in kwargs.items():
            text = re.sub(r"\{" + re.escape(k) + r"\}", str(v).replace("\\", "\\\\"), text)
        return PromptTemplate(text)
