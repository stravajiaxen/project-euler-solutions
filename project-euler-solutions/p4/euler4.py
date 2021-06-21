"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #4 Largest palindrome product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    return str(num) == "".join(list(reversed(str(num))))

def main():
    pals = []  # I have no pals :(

    for a in range(100, 1000):
        for b in range(100, 1000):
            prod = a*b

            if is_palindrome(prod):
                pals.append(prod)

    print(sorted(pals))
    print(max(pals))

if __name__ == '__main__':
    main()