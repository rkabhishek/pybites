import math

def round_up_or_down(transactions, up=True):
    return [math.ceil(t) if up else math.floor(t) for t in transactions]
