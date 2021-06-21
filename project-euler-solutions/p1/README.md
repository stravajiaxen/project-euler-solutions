# Euler 1: Multiples of 3 and 5

## Description

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Solution
This problem is pretty simple. I just run through each number,
check if it's a multiple of 3 or 5 and add it to a running total
if it is.

I bet there's a one liner using `sum` and a list comprehension...

`print(sum([i for i in range(1000) if (not (i % 3)) or (not (i % 5))]))`