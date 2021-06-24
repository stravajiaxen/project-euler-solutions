
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #27 Quadratic primes

Euler discovered the remarkable quadratic formula:

$n^2 + n + 41$

It turns out that the formula will produce 40 primes for the consecutive integer
values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$
is divisible by 41, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by 41.

The incredible formula $n^2 - 79n + 1601$ was discovered, which produces 80 primes for
the consecutive values $0 \le n \le 79$. The product of the coefficients, 79 and 1601,
is 126479.

Considering quadratics of the form:

Find the product of the coefficients, $a$ and $b$, for the quadratic expression that
produces the maximum number of primes for consecutive values of $n$, starting with
$n = 0$.
"""
import time
from sympy.ntheory import isprime

def get_quad(a, b):

    def formula(x):
        return x*x + a*x + b

    return formula

def main():

    formulae_results = {}

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            f = get_quad(a, b)
            i = 0
            while(isprime(f(i))):
                i += 1
            formulae_results[(a, b)] = i

    things = []
    for (a, b), i in formulae_results.items():
        things.append([a, b, i])
    result = sorted(things, key=lambda x: x[2], reverse=True)[0]
    print(result[0] * result[1])
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
