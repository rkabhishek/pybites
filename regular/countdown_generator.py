def countdown():
    n = 100
    while n >= 1:
        yield n
        n -= 1
