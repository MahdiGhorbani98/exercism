from datetime import datetime
from datetime import timedelta

def add(moment):
    new_data = moment + timedelta(seconds=1_000_000_000)
    return new_data