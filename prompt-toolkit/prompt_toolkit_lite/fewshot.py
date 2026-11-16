from .template import PromptTemplate


def few_shot(instruction: str, examples: list[dict], example_template: str, query: dict) -> str:
    """Compose a few-shot prompt from an instruction, examples and a query."""
    ex = PromptTemplate(example_template)
    parts = [instruction.strip()] + [ex.render(**e) for e in examples] + [ex.partial(**query).template]
    return "\n\n".join(parts)
