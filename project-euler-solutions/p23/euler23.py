
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #23 Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it
is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that
can be written as the sum of two abundant numbers is 24. By mathematical analysis,
it can be shown that all integers greater than 28123 can be written as the sum of two
abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two
abundant numbers.
"""
import time
import functools
import math

@functools.lru_cache
def is_abundant(num):
    return sum(proper_divisors(num)) > num

@functools.lru_cache
def proper_divisors(num):
    return divisors(num) - {num}

@functools.lru_cache  # Should cache results
def divisors(num):
    if num == 1:
        return {1}
    if num == 2:
        return {1, 2}
    if num == 3:
        return {1, 3}
    if num == 4:
        return {1, 2, 4}

    max_num = int(math.ceil(num ** 0.5))
    divs = []
    for i in range(1, max_num+1):
        if num % i == 0:
            divs.append(i)
    return set(divs + [num//div for div in divs])

def main():
    abundant_nums = []
    max_num = 28123
    for i in range(1, max_num):
        if is_abundant(i):
            abundant_nums.append(i)

    even_abundant_nums = [i for i in abundant_nums if i%2 == 0]
    odd_abundant_nums = [i for i in abundant_nums if i%2 == 1]
    # There are fewer odd ones

    non_abundant_sums = list(range(1, 28124))
    tot = 0
    for nonab in non_abundant_sums:
        print(nonab)

        if nonab %2 == 0: # Even -- check only sums of even numbers
            for ab in even_abundant_nums:
                if nonab - ab in even_abundant_nums:
                    tot -= nonab
                    break
                if ab > nonab:
                    break
        if nonab %2 != 0: # Odd -- subtract only the odd numbers
            for ab in odd_abundant_nums:
                if nonab - ab in even_abundant_nums:
                    tot -= nonab
                    break
                if ab > nonab:
                    break
        tot += nonab



    # Still takes too long!!

    # non_abundant_sums = list(range(1, 28124))
    # tot = 0
    # for nonab in non_abundant_sums:
    #     print(nonab)
    #     for ab in abundant_nums:
    #         if nonab - ab in abundant_nums:
    #             tot -= nonab
    #             break
    #     tot += nonab

    # Takes too long!!

    # for i in range(len(abundant_nums)):
    #     for j in range(i, len(abundant_nums)):
    #         if abundant_nums[i]+abundant_nums[j] in non_abundant_sums:
    #             non_abundant_sums.remove(abundant_nums[i]+abundant_nums[j])

    print(tot)
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
