import string

alphanumeric_chars = set(string.ascii_letters + string.digits)


def get_index_different_char(chars: list[str | int]) -> int:
    count = {True: 0, False: 0}
    first_index = {True: -1, False: -1}

    for index, c in enumerate(chars):
        isalnum = str(c) in alphanumeric_chars
        if count[isalnum] == 0:
            if count[not isalnum] <= 1:
                count[isalnum] = 1
                first_index[isalnum] = index
            else:
                return index
        else:
            if count[not isalnum] == 0:
                count[isalnum] += 1
            else:
                return first_index[not isalnum]

    raise ValueError("No different character found")
