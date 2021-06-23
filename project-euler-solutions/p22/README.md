
# Euler 22: Names scores

## Description
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?

## Solution
*871198282*

Python makes a lot of these solutions elegant. Want to sort some names? try `sorted(names)`
Want to find the value of a character? Try `ord(c) - ord('A') + 1`. It's just deadly simple.
Combine that with the ease of reading the file... I weep for the C programmers attempting
this one.

At least C made it easy to convert letters to numbers... I think?