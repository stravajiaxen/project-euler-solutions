
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net) Problem #15 Lattice paths

Starting in the top left corner of a 2x2 grid, and only being able to move to the
right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""
import time


def main():
    solns = {(i, j): None for i in range(1, 21) for j in range(1, 21)}
    for i in range(1, 21):
        solns[(i, 1)] = i+1
        solns[(1, i)] = i+1


    def solns_for(i, j):
        if solns[(i, j)] is not None:
            return solns[i, j]
        else:
            if i == 1:
                solns[i, j] = j+1
                return solns[i, j]
            if j == 1:
                solns[i, j] = i+1
                return solns[i, j]
            else:
                solns[i, j] = solns_for(i-1, j) + solns_for(i, j-1)
                return solns[i,j]

    print(solns_for(20, 20))
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
