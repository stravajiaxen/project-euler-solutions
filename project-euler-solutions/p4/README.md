
# Euler 4: Largest palindrome product

## Description
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

## Solution
*906609*

This one was a little tricky:

1. Remembering how to reverse a string in Python was less than as trivial as I thought it'd be. I thought `reversed()` would just work.
It didn't. I ended up with an `is_palindrome` function that returned
`str(num) == "".join(list(reversed(str(num))))`. 

2. I should've known better on this one. I tried to do zip() instead of a double-for loop. It led to
some 3 minutes of debugging to find the solution...

Otherwise, the answer is straightforward. It's trivial for a computer to try 900**2 unique combinations, even disregarding
cumulative properties, and whatnot... Brute-force wins this round