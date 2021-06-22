
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net) Problem #10 Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def main():
    all_nums = [None, None] + list(range(2, 2000000))
    primes = []

    for i, val in enumerate(all_nums):
        if val is None:
            continue
        else:
            primes.append(val)
            cur = val
            while cur < len(all_nums):
                all_nums[cur] = None
                cur += val

    print(primes)
    print(sum(primes))
    
if __name__ == "__main__":
    main()
