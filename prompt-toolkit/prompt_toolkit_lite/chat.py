class ChatPrompt:
    """Builds a list of role/content messages for chat-style LLM APIs."""
    ROLES = {"system", "user", "assistant"}

    def __init__(self):
        self.messages = []

    def add(self, role: str, content: str) -> "ChatPrompt":
        if role not in self.ROLES:
            raise ValueError(f"Unknown role: {role}")
        self.messages.append({"role": role, "content": content})
        return self

    def system(self, c): return self.add("system", c)
    def user(self, c): return self.add("user", c)
    def assistant(self, c): return self.add("assistant", c)

    def to_list(self):
        return list(self.messages)
