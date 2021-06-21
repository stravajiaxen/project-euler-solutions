
# Euler 9: Special Pythagorean triplet

## Description
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.

## Solution
*31875000*

375, 200, 425 is the triple

This one was actually really straight-forward, but there are some pitfalls.

If you try to just iterate with a triple for-loop, you'll take a long time (though not crazy long, in fact. Computers are fast!)
If you do a double for loop and choose a, b, and c in such a way that c isn't greater than a and b, you'll also be out of luck.

Otherwise, it's basically the loop I did in the program:

```python
    for a in range(3, 1000):
        for b in range(1, a):
            c = 1000 - a - b

            if a**2 + b**2 == c**2:
                print(a, b, c, a*b*c)
```

5 lines! (6 if you count whitespace)