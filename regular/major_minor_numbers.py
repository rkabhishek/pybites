from collections import Counter


def major_n_minor(numbers):
    counts = Counter(numbers)

    major = max(numbers, key=lambda x: counts[x])
    minor = min(numbers, key=lambda x: counts[x])

    return major, minor
