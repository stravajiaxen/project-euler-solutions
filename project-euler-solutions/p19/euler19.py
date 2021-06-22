
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net) Problem #19 Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import time
import datetime  # Yeah, I'm cheating


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
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
