def split_in_columns(message):
    lines = message.split('\n')
    return '|'.join(lines)
