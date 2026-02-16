def round_to_next(number: int, multiple: int):
    remainder = number % multiple
    if remainder == 0:
        return number
    else:
        diff = multiple - remainder
        return number + diff
