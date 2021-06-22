
# Euler 16: Power digit sum

## Description
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

## Solution
*1366*

Another one that Python makes trivially easy:

```python
print(sum([int(i) for i in str(2**1000)]))
```