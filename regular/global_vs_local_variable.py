num_hundreds = -1

def sum_numbers(numbers: list) -> int:
    global num_hundreds
    total = sum(numbers)
    num_hundreds += total // 100
    return total
