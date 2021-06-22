
# Euler 13: Large sum

## Description
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

## Solution
*5537376230*

This is completely trivial in Python, of course. Add them up and then take a substring.

If we had to be clever about it, we might start by taking the largest digits
of the numbers, but not the whole numbers themselves, and add those up only. Luckily we didn't
have to :)