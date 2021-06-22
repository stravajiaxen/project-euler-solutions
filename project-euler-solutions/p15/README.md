
# Euler 15: Lattice paths

## Description
Starting in the top left corner of a 22 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 2020 grid?

## Solution
*137846528820*

Ah, recursion.

This problem was begging for a recursive solution. It took me a bit to figure
out exactly what the recursive step was, but it wasn't too hard once I thought about what
a base case might look like. I considered a long Tetris "I" piece-like shaped grid
and then considered what it'd look like if I were to go wider or if I were to go taller.