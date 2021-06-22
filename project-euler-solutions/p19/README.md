
# Euler 19: Counting Sundays

## Description
You are given the following information, but you may prefer to do some research for yourself.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

## Solution
*171*

Dealing with days of the week in Python is common enough that
the `datetime` module was created to deal with it. Using some
clever `__gt__` and `__lt__` comparisons makes the source code
incredibly obvious even!

I could have done it myself the manual way but using `datetime` was wayyy easier!

```python
import datetime

def main():
    current_date = datetime.date(month=1, day=1, year=1901)
    last_date = datetime.date(month=12, day=31, year=2000)

    SUNDAY = 6  # According to https://docs.python.org/3/library/datetime.html#datetime.date.weekday 

    days = 0

    one_day = datetime.timedelta(days=1)

    while current_date < last_date:
        if current_date.day == 1 and current_date.weekday() == SUNDAY:
            days += 1
        current_date += one_day

    print(days)
    
```