
# Euler 27: Quadratic primes

## Description
Euler discovered the remarkable quadratic formula:

$n^2 + n + 41$

It turns out that the formula will produce 40 primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by 41, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by 41.

The incredible formula $n^2 - 79n + 1601$ was discovered, which produces 80 primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.

## Solution
*-59231*

Armed with the knowledge that `sympy` has a pretty nice `isprime` function
I decided to make use of that in this problem. This was pretty easy
once I did.