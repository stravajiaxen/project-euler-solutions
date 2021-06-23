
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #25 1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:

Hence the first 12 terms will be:

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time


def main():
    fibs = [1, 1, 2, 3, 5]
    while len(str(fibs[-1])) < 1000:
        fibs.append(fibs[-1] + fibs[-2])

    print(len(fibs))
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
