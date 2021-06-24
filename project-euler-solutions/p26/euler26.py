"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #26 Reciprocal cycles

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its
decimal fraction part.
"""
import time

# Based on some code from:
# https://stackoverflow.com/questions/25181642/how-set-numpy-floating-point-accuracy
import sympy as smp
import mpmath as mp


def main():
    mp.mp.dps = 3000  # Computation precision is 1000 digits

    num = mp.mpf("1.0")
    for i in range(1, 1001):

        den = mp.mpf(str(i))
        # print(f"1/{i} = ", num/den)
        val = str(num/den)
        for offset in range(1, 1000):
            for cycle_size in range(1, 1000):
                raise NotImplementedError("I was able to solve this one from my research!")
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
