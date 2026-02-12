import math

def round_up_or_down(transactions, up=True):
    rounding = math.ceil if up else math.floor
    return [rounding(t) for t in transactions]
