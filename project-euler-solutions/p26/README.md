
# Euler 26: Reciprocal cycles

## Description
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

## Solution
*983*

It's funny. I guessed on this one after doing some research on repeating decimals. But it makes sense
after I thought about it a little!


There's a related concept to repeating decimals called a cyclic number where 1/n has a repeating decimal of size
(n-1). 7 is the first such number. It's called "cyclic" because 2/7 is just like 1/7 except the
last digit becomes the first and it continues.

On the [Wikipedia page on Cyclic Numbers](https://en.wikipedia.org/wiki/Cyclic_number) they give an example
list of cyclic numbers and list the ones after 7. One off them is 983. Just for funsies, I put it into
Project Euler and I got that pretty green checkmark.

I was doing this research because I was trying to loop over all the numbers, making use of 
`mpmath` to expand the size of the decimal that python would print out so I could iterate over
some potential denominators to see which gave the longest repeating decimal. I needed to know which
ones I could skip. For each number I couldn't skip, I was going to then skip to the correct starting
position (`[0]` if it's <10, `[1]` if it's < 100, `[2]` otherwise) then iterate
over some potential offsets and cycle sizes until I could determine the appropriate
repetition length. This might have required some cleverness to get right (i.e. how do you know that something has
a repetend length of 1? do you only need to check the immediate next digit?)

Oh, I also found out more about what `sympy` can do. Apparently it would
have made a bunch of these problems trivial... if I wanted to use it :)