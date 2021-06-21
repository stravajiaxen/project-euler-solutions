
# Euler 5: Smallest multiple

## Description
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## Solution
*232792560*

I did this one basically without a computer. I just used it to calculate the product
of the constituent factorization: `[2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]`

How'd I get that list?

The prime factorization of the answer is the smallest set that contains the prime factorization of each
number 1-20 as a subset. So...

1. Take the prime factorization of each number 1-20
2. Construct a set by adding missing pieces of the set from each prime factorization into the
target prime factorization (you have to add duplicates)
3. Take the product of all those prime factors -- that's the answer