
# Euler 7: 10001st prime

## Description
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

## Solution
*104743*

I think I did this in a less-than-optimal way. It took a couple seconds for python
to terminate... I probably could have stopped at the square root of the number rather than
going up through all the prime numbers so far. Oh well, it worked! TODO: Refactor the code
to stop sooner.

In any case, I iterate through numbers from 1 until I have at least 10001 prime numbers.
I check each prospective new number against all the prime numbers (TODO: Stop at `sqrt(cur_num)`) and if it
doesn't find that any are divisors, it must be prime.