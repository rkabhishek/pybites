def count_indents(text: str) -> int:
    count = 0
    for ch in text:
        if ch == ' ':
            count += 1
        else:
            break

    return count

def count_indents_using_length(text: str) -> int:
    return len(text) - len(text.lstrip(" "))
