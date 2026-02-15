from datetime import date
from datetime import timedelta


def tomorrow(today=None):
    if today is None:
        today = date.today()

    return today + timedelta(days=1)
