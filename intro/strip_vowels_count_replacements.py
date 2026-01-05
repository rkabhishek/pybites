VOWELS = 'aeiou'

def strip_vowels_build_list(text: str) -> tuple[str, int]:
    vowel_count = 0
    result = []
    for ch in text:
        if ch.lower() in VOWELS:
            result.append('*')
            vowel_count += 1
        else:
            result.append(ch)

    return ''.join(result), vowel_count


def strip_vowels_generator(text: str) -> tuple[str, int]:
    result = ('*' if ch.lower() in VOWELS else ch for ch in text)
    vowel_count = sum(1 for ch in text if ch.lower() in VOWELS)
    return ''.join(result), vowel_count
