
# Euler 25: 1000-digit Fibonacci number

## Description
The Fibonacci sequence is defined by the recurrence relation:

Hence the first 12 terms will be:

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

## Solution
*4782*

This is really dead-easy in python. Luckily it can handle integers with
ridiculously large sizes.

When `fibs` is filled with the fibonacci sequence up to the one that has at least
1000 digits, then the length of the list is the index of that element.


```python
def main():
    fibs = [1, 1, 2, 3, 5]
    while len(str(fibs[-1])) < 1000:
        fibs.append(fibs[-1] + fibs[-2])

    print(len(fibs))
```