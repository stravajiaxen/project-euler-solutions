
# Euler 24: Lexicographic permutations

## Description
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012 021 102 120 201 210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

## Solution
*2783915460*

There's a nifty library called `itertools` in python that's good at making
these kinds of permutations. I usually use it for making DOEs by using the `product` method
but `permutations` is the kind we want here. It turns out that it produces them
in lexicographical order if you just use it outright.

We want the 1,000,000 permutation (index of 999,999) of length 10 of the string
`"0123456789"`. Then join it back into a single item and... you're all set.

Answered in 1 line! (after the import statement)

```python
print("".join(list(itertools.permutations("0123456789", 10))[999999]))
```