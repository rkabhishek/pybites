from typing import Union

def convert(value: Union[int, float], fmt: str) -> float:
    if type(value) not in (int, float):
        raise TypeError(f"{value} must be an int or float")

    fmt = fmt.lower()
    if fmt not in ("cm", "in"):
        raise ValueError(f"fmt must be either 'cm' or 'in'")

    if fmt == "cm":
        return round(value * 2.54, 4)
    else:
        return round(value / 2.54, 4)
