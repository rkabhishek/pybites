def rotate(string, n):
    cycle_length = len(string)
    n = n % cycle_length
    return string[n:] + string[:n]
