PYBITES = "pybites"

def convert_pybites_chars(text):
    converted = [ ch.swapcase() if ch.lower() in PYBITES else ch for ch in text]
    return ''.join(converted)
