from collections import defaultdict

def freq_digit(num: int) -> int:
    counts = defaultdict(int)
    num = str(abs(num))

    result = None
    max_freq = 0

    for c in num:
        counts[c] += 1
        if counts[c] > max_freq:
            max_freq = counts[c]
            result = c

    return int(result)
