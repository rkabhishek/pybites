VOWELS = 'aeiou'
PYTHON = 'python'

VOWEL_SET = set(VOWELS)
PYTHON_SET = set(PYTHON)

def contains_only_vowels(input_str):
    input_str = input_str.lower()
    return all(ch in VOWEL_SET for ch in input_str)


def contains_any_py_chars(input_str):
    input_str = input_str.lower()
    return any(ch in PYTHON_SET for ch in input_str)


def contains_digits(input_str):
    return any(ch.isdigit() for ch in input_str)
