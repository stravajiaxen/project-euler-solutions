
# Euler 6: Sum square difference

## Description
The sum of the squares of the first ten natural numbers is, 385

The square of the sum of the first ten natural numbers is, 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Solution
*25164150*

It helped to remember that the sum from 1 to n is `(n * (n+1)) / 2`

This was trivial. Write a for-loop to get the squares (probably could've used a comprehension), do the
magic formula and square it for the square of the sum. Then take the difference.