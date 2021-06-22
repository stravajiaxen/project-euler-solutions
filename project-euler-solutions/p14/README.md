
# Euler 14: Longest Collatz sequence

## Description
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

## Solution
*837799*

OK. This one took 5 minutes through brute force (`main`)

I started to build a different approach while waiting for `main` to complete. I creatively
called it `main2`. The *main* difference is that each time I get a sequence back, I just iterate through
it and list the time to get to each number in the sequence and store it instead of having to calculate
the full sequence any time. That way, if I've already encountered that number from another sequence, I don't have
to figure it out again.

`main2` takes only 47s to run -- a nifty 6x speed :)