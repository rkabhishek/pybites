from string import ascii_lowercase

def slice_and_dice(text: str) -> list[str]:
    lines = text.strip().split('\n')
    results = []
    for line in lines:
        line = line.lstrip()
        if line and line[0] in ascii_lowercase:
            words = line.split()
            last_word = words[-1].rstrip('.!')
            results.append(last_word)

    return results
