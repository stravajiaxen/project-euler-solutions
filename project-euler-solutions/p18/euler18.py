"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net) Problem #18 Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

37 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

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

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""
import time
import networkx as nx

def main():
    triangle = \
'''75
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
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

    # Construct a graph
    G = nx.DiGraph()

    G.add_node("source")
    G.add_node("sink")

    triangle = [[int(i) for i in line.split()] for line in triangle.split("\n")]

    # Store vals to make it easy to add up the best path at the end
    vals = {}

    # Constructing the graph edges with weights
    for i, row in enumerate(triangle):
        for j, val in enumerate(row):
            print(val)
            G.add_node((i, j))
            vals[(i, j)] = val
            if i == 0:
                G.add_edge("source", (i, j), weight=100-val, num=val)  # 100-val lets us make it a minimization problem
            else:
                if j == 0: # Don't do j-1
                    G.add_edge((i-1, j), (i, j), weight=100-val, num=val)
                if j == i: # Don't do j+1
                    G.add_edge((i-1, j-1), (i, j), weight=100-val, num=val)
                if j!=0 and j!= i: # Add two edges
                    G.add_edge((i-1, j-1), (i, j), weight=100-val, num=val)
                    G.add_edge((i-1, j), (i, j), weight=100-val, num=val)

    # Connect to the sink
    for j, val in enumerate(triangle[-1]):
        G.add_edge((len(triangle)-1, j), "sink", weight=100-val, num=val)

    path = nx.dijkstra_path(G, "source", "sink")

    # Sum up the vals of the edges along the best path.
    tot = 0
    for edge in path:
        if edge != "source" and edge != "sink":
            tot += vals[edge]

    print(tot)
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
