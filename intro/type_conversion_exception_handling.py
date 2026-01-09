def divide_numbers(numerator, denominator):
    try:
        return int(numerator) / int(denominator)
    except ValueError:
        raise ValueError("Can only divide two numbers")
    except ZeroDivisionError:
        return 0
