def positive_divide(numerator, denominator):
    try:
        res = numerator / denominator
    except ZeroDivisionError:
        return 0

    if res < 0:
        raise ValueError("Result must be positive")

    return res
