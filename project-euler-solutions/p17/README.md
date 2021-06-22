
# Euler 17: Number letter counts

## Description
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

## Solution
*21124*

This one was pretty rigorous to do but not difficult. I probably
saved myself a headache by typing out the numbers and using `len` rather than
trying to just map the numbers without thinking about the number they represent.

I did actually run into a bug on this one. It was related to line 63:

```python
return len(tens[tens_place]) + (0 if ones_place == 0 else letters_in(ones_place))
```

I hadn't added the parentheses around the `(0 if ones_place == 0 else letters_in(ones_place))` segment at first
and surprisingly python actually interpreted it successfully but with a logic error. It was the
first place I looked after projecteuler threw up, but I guess this is a good case to remember to use parentheses liberally (even when you don't have to (seriously))

( ;-) )