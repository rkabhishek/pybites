VOWELS = 'aeiou'

def strip_vowels(text: str) -> tuple[str, int]:
    vowel_count = 0
    text_as_list = list(text)
    for i, ch in enumerate(text_as_list):
        if ch.lower() in VOWELS:
            text_as_list[i] = '*'
            vowel_count += 1

    return "".join(text_as_list), vowel_count
