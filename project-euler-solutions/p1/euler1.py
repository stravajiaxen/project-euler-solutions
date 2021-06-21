def main():
    mults = [3, 5]

    tot = 0

    for i in range(0, 1000):
        for mult in mults:
            if i % mult == 0:
                tot += i
                break

    print(tot)

if __name__ == '__main__':
    main()