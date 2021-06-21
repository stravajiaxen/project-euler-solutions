def main():
    mults = [3, 5]

    tot = 0

    for i in range(0, 1000):
        for mult in mults:
            if i % mult == 0:
                tot += i
                break

    print(tot)

def dumb_one_liner():
    print(sum([i for i in range(1000) if (not (i % 3)) or (not (i % 5))]))

if __name__ == '__main__':
    main()