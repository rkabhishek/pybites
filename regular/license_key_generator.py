import random
import string

POOL = string.ascii_uppercase + string.digits

def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    if parts <= 0 or chars_per_part <= 0:
        raise ValueError('parts and chars_per_part must be positive')

    result = []
    for _ in range(parts):
        part = ''.join(random.choice(POOL) for _ in range(chars_per_part))
        result.append(part)

    return '-'.join(result)
