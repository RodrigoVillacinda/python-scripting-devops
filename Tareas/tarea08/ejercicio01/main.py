#!/usr/bin/env python3


def main():

    sum = 0
    with open("indata.txt") as f:
        for x in f:
            sum += float(x)
    print(f"{sum:,.2f}")

if __name__ == "__main__":
    main()
