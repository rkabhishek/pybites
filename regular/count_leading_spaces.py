def count_indents(text: str) -> int:
    return len(text) - len(text.lstrip(" "))
