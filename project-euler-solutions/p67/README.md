
# Euler 67: Maximum path sum II

## Description
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

37 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

## Solution
*7273*

I intend to solve this and Problem 618 at once. This appears to be possible to do with a path-finding algorithm (e.g. dijkstra's algorithm or A*)

This problem is a bit unique in that I want to *maximize* the value at the end rather than
minimize it, but I can turn it into a minimization problem by subtracting 100 - `num` for each `num` in the list and minimizing
the path to the bottom if those are the weights of edges on a graph. The path that minimizes
that number will be the one that maximizes the possible amount.

(Finished this! The above worked just perfectly.)

