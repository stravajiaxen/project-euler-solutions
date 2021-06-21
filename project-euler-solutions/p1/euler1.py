"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #1 Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main():
    mults = [3, 5]

    tot = 0

    for i in range(0, 1000):
        for mult in mults:
            if i % mult == 0:
                tot += i
                break

    print(tot)

def dumb_one_liner():
    print(sum([i for i in range(1000) if (not (i % 3)) or (not (i % 5))]))

if __name__ == '__main__':
    main()