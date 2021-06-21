
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #9 Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""


def main():
    for a in range(3, 1000):
        for b in range(1, a):
            c = 1000 - a - b

            if a**2 + b**2 == c**2:
                print(a, b, c, a*b*c)
    
    
if __name__ == "__main__":
    main()
