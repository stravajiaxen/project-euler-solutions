
# Euler 21: Amicable numbers

## Description
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

## Solution
*31626*

I was worried about the runtime from the get go so I decided to cache
results from my divisors function. This ended up being fine. Since `functools`
made it so easy with a decorator, I decided to also cache `d(n)` (my worst function
name ever written).

Caching was probably a good idea. It still took 14.5s on my computer to complete.

I could have gone about this an entirely different way! I could have generated
divisors for all numbers which would have taken O(n**1.5) by iterating through
numbers from 1 to root(n) and for each of those numbers start counting up by that number
up to n (n = 10000) and append to some global array all of the divisors of that number.

Something like...
```python
import math
max_num = 10000
factors = {i: [] for i in range(1, max_num+1)}

for factor in range(1, math.ceil(math.sqrt(max_num))):
    cur_num = factor
    i = 1
    while factor < max_num:
        factors[cur_num].append(i)
        cur_num += factor
        i += 1
```