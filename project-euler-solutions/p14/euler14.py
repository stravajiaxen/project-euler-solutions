
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net)
Problem #14 Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time

def get_seq(i):
    seq = [i]
    next = i
    while seq[-1] != 1:
        next = next_term(next)
        seq.append(next)
    return seq

def next_term(num):
    if num % 2 == 0:
        return num//2
    else:
        return 3 * num + 1

def main2():
    max_num = 1000000
    nums = {}
    nums[0] = [1, 0]
    nums[1] = [4, 1]
    nums[2] = [1, 2]

    for i in range(0, max_num):
        if not nums.get(i):
            seq = get_seq(i)
            for x, num in enumerate(seq[:-1]):
                # print(seq[x+1], len(seq)-x-2)
                nums[num] = [seq[x+1], len(seq)-x-1]

    chains = []
    for num, (_, chain_length) in nums.items():
        if num < max_num:
            chains.append((num, chain_length))
    print(sorted(chains, reverse=True, key=lambda c: c[1])[0][0])  # The number whose chain is longest is first



def main():
    nums = {}
    max_num = 1000000
    for i in range(2, max_num):  # 1 is trivial
        nums[i] = get_seq(i)

    chains = []
    for num, chain in nums.items():
        chains.append((num, chain))
    print(sorted(chains, reverse=True, key=lambda c: len(c[1]))[0][0])  # The number whose chain is longest is first
    
if __name__ == "__main__":
    start_time = time.time()
    main2()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
