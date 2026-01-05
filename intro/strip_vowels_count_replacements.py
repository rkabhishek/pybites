VOWELS = 'aeiou'

def strip_vowels(text: str) -> tuple[str, int]:
    vowel_count = 0
    result = []
    for ch in text:
        if ch.lower() in VOWELS:
            result.append('*')
            vowel_count += 1
        else:
            result.append(ch)

    return ''.join(result), vowel_count
