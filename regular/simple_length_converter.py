from typing import Union

FORMATS = {"cm": 2.54, "in": 0.3937007874}

def convert(value: Union[int, float], fmt: str) -> float:
    if type(value) not in (int, float):
        raise TypeError(f"{value} must be an int or float!")

    fmt = fmt.lower()
    if fmt not in FORMATS:
        raise ValueError(f"{fmt} is an unsupported format!")

    return round(value * FORMATS[fmt], 4)
