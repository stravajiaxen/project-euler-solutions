
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #21 Amicable numbers

Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import time
import math
import warnings
import functools

def test():
    import math
    max_num = 10000
    factors = {i: [] for i in range(1, max_num + 1)}

    for factor in range(1, math.ceil(math.sqrt(max_num))):
        cur_num = factor
        i = 1
        while cur_num < max_num:
            factors[cur_num].append(i)
            cur_num += factor
            i += 1
    print(factors[20])

@functools.lru_cache
def d(n):
    """Sum of the proper divisors of N (according to Project Euler)"""
    return sum(divisors(n)) - n  # Divisors adds N -- just want the proper divisors


@functools.lru_cache  # Should cache results
def divisors(num):
    if num == 1:
        return [1]
    if num == 2:
        return [1, 2]
    if num == 3:
        return [1, 3]
    if num == 4:
        return [1, 2, 4]

    max_num = int(math.ceil(num ** 0.5))
    divs = []
    for i in range(1, max_num+1):
        if num % i == 0:
            divs.append(i)
    return set(divs + [num//div for div in divs])


def main():
    amicable_nums = []
    for a in range(10000):
        for b in range(10000):
            if a == b:
                continue
            if d(a) == b and d(b) == a:
                amicable_nums.append(a)
                amicable_nums.append(b)

    print(sum(set(amicable_nums)))

    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
