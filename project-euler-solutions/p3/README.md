
# Euler 3: Largest prime factor

## Description
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

## Solution

*6857*

This one was fun. It turns out I accidentally solved it correctly right away.
I just didn't believe I had it right.

Another one where a bit of math cleverness helps. If you start iterating through (prime) numbers
and divide 600851475143 each time by the number, it will lower the max number each time. You can stop
when your current prime number is <= the current max number.
