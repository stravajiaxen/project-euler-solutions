
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #17 Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""
import time

letters = [
    "",  # Makes the base easy!
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

tens = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def letters_in(num):
    if num < 20:
        return len(letters[num])
    elif num < 100:
        tens_place, ones_place = int(str(num)[0]), int(str(num)[1])
        return len(tens[tens_place]) + (0 if ones_place == 0 else letters_in(ones_place))
    # elif num == 100:
    #     return len("onehundred")
    elif num < 1000:
        hundreds_place, tens_place, ones_place = int(str(num)[0]), int(str(num)[1]), int(str(num)[2])
        if tens_place == 0 and ones_place == 0:
            return letters_in(hundreds_place) + len("hundred")
        else:
            return letters_in(hundreds_place) + len("hundredand") + letters_in(10*tens_place + ones_place)
    else:
        assert num == 1000
        return len("onethousand")


def main():
    tot = 0
    for i in range(1, 1001):
        tot += letters_in(i)
    print(tot)
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
