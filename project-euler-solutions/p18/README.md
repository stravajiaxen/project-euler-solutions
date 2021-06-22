
# Euler 18: Maximum path sum I

## Description
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

37 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
```
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
```
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

## Solution
*1074*

I intend to solve this and Problem 67 at once. This appears to be possible to do with a path-finding algorithm (e.g. dijkstra's algorithm or A*)

This problem is a bit unique in that I want to *maximize* the value at the end rather than
minimize it, but I can turn it into a minimization problem by subtracting 100 - `num` for each `num` in the list and minimizing
the path to the bottom if those are the weights of edges on a graph. The path that minimizes
that number will be the one that maximizes the possible amount.

(Finished this! The above worked just perfectly.)
