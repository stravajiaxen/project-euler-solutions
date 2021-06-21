
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net) Problem #7 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

primes = [2, 3]

def main():
    cur_val = 3  # Next on the list after 3 -- prime number
    while len(primes) < 10001:
        cur_val += 1
        is_prime = True
        for i in primes:
            if cur_val % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(cur_val)

    print(primes[10000])  # Careful not to be off-by-one!


if __name__ == "__main__":
    main()
