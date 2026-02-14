from collections import defaultdict

def freq_digit(num: int) -> int:
    counts = defaultdict(int)
    num = str(num)

    for c in num:
        counts[c] += 1

    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return int(sorted_counts[0][0])
