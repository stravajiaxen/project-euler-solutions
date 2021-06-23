
# Euler 23: Non-abundant sums

## Description
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

## Solution
*4179871*

I loved this one.

This one required me to be clever to get it to run quickly. I'm proud of the solution (which takes 10.9s to run).

I didn't bother with the commented out blocks of code which were taking too long to run, but they're in the code still, commented out.

We know that 28123 is special in that every number above it can be shown to be the sum of two abundant numbers. Finding
abundant numbers below 28123 is the first goal, then. We can stop at 28123 because any abundant numbers higher than it
won't matter for this problem. We want to find all the numbers which *cannot* be written as the sum of two
abundant numbers -- since they're all positive, any numbers above that max of 28123 can't contribute to helping
us find numbers that aren't the sum of abundant numbers.

So, the first part gets us abundant numbers. That's pretty easy. The hard part of the problem
was actually computing which of the numbers below 28123 cannot be written as the sum of two abundant numbers.

There are some 6,400ish abundant numbers (I forgot the total length). That gives us some 20 million combinations of numbers
if we want to just try every possible combination to see which give us numbers that *can* sum up from two
smaller abundant numbers. This will take too long as I quickly found out.

I ultimately took a different approach. I split the abundant numbers into evens and odds and used a different strategy
based on the parity of each number I was trying to figure from 1 to 28123. If it's even, I wanted to check if it could be the
sum of two even numbers. If it were odd, I wanted to check if it could be the sum of an odd and an even number. To do this,
I *subtracted* each even or odd abundant number (depending on parity) and checked if the difference were in the even_abundant_numbers
list. For odd numbers it's better to subtract each number from the odd_abundant numbers list since there are fewer of them.
I also (actually while writing this readme realized this optimization!) would break whenever I found the current
abundant number was greater than the target number (since the abundant number lists were sorted).


```python
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

```
