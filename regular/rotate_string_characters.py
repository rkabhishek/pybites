from collections import deque

def rotate(string, n):
    cycle_length = len(string)
    n = n % cycle_length
    return string[n:] + string[:n]

def rotate_deque(string, n):
    d = deque(string)
    d.rotate(-n)
    return ''.join(d)
