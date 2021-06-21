
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #6 Sum square difference

The sum of the squares of the first ten natural numbers is, 385

The square of the sum of the first ten natural numbers is, 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is $3025 - 385 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
"""

def main():
    squares = []
    for i in range(1, 101):
        squares.append(i*i)

    sq_sum = ((100 * 101) / 2) ** 2

    print(sq_sum - sum(squares))



if __name__ == '__main__':
    main()