from typing import List, TypeVar, Union
from math import floor
from math import log10
Number = Union[int, float]
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    return [_convert_to_n_digit(x, n) for x in numbers]


def _convert_to_n_digit(num: Number, n: int) -> int:
    if n < 1:
        raise ValueError('n should be a positive integer')
    if num == 0:
        return 0
    else:
        return int(num * (10 ** (n - get_magnitude(num))))


def get_magnitude(num: Number) -> int:
    if num == 0:
        raise ValueError("Magnitude undefined for zero")
    num = abs(num)
    return floor(log10(num)) + 1
