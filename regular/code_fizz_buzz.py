from typing import Union

def fizzbuzz(num: int) -> Union[str, int]:
    result = ''
    if num % 3 == 0:
        result += 'Fizz'
    if num % 5 == 0:
        if result != '':
            result += ' '
        result += 'Buzz'

    if result == '':
        result = num

    return result

def fizzbuzz2(num: int) -> Union[str, int]:
    parts = []
    if num % 3 == 0:
        parts.append('Fizz')
    if num % 5 == 0:
        parts.append('Buzz')

    if parts:
        return ' '.join(parts)
    else:
        return num
