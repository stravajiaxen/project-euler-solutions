"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #3 Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# I'm sure numpy has a prime factorization module. Let's do this the fun way first

def factors_of(num):

    if num <= 2:
        return []

    val = 2

    factors = []

    while val <= num:
        if num % val == 0:
            factors.append(val)
            num /= val
        val += 1

    if factors == []:
        return [num]
    return factors

def prime_factorization(num):
    # Turns out my factors_of function gives a prime factorization... This function was unnecessary.
    factors = factors_of(num)
    if factors == [num]:
        return [num]
    else:
        for factor in reversed(factors):  # I assume bigger numbers are less likely to be prime
            x = factors_of(factor)
            print(x)
            if x != [factor]:
                return set([prime_factorization(i) for i in x])


def main():
    the_big_kahuna = 600851475143
    print(factors_of(the_big_kahuna))
    print(max(factors_of(the_big_kahuna)))


if __name__ == '__main__':
    main()