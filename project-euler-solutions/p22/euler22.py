
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net) Problem #22 Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
over five-thousand first names, begin by sorting it into alphabetical order. Then
working out the alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938x53 = 49714.

What is the total of all the name scores in the file?
"""
import time

def name_score(i, name):
    tot = 0
    for c in name:
        val = ord(c) - ord('A') + 1
        tot += val
    return (i * tot)


def main():
    fname = "p022_names.txt"
    with open(fname, 'r') as f:
        content = f.read()
    names = content.split(",")
    names = [name.strip('"') for name in names]
    names = sorted(names)

    tot = 0
    for i, name in enumerate(names):
        tot += name_score(i+1, name)
    print(tot)
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
