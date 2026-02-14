def is_armstrong(n: int) -> bool:
    if n < 0:
        return False

    s = str(n)
    power = len(s)

    total = sum(int(d) ** power for d in s)

    return total == n
