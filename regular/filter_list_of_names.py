IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5

def filter_names(names):
    result = []
    for name in names:
        if name.startswith(IGNORE_CHAR) or any(c.isdigit() for c in name):
            continue
        if name.startswith(QUIT_CHAR) or len(result) >= MAX_NAMES:
            break

        result.append(name)

    return result
