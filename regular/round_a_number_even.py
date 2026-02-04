import math

def round_even(number):
    if number - math.floor(number) == 0.5:
        return round_midpoint(number)
    else:
        return round_by_distance(number)


def round_midpoint(number):
    integer = math.floor(number)
    if integer % 2 == 0:
        return integer
    else:
        return integer + 1

def round_by_distance(number):
    integer = math.floor(number)
    distance = number - integer
    if distance > 0.5:
        integer = integer + 1

    return integer
