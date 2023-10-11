#!/usr/bin/python3

from sys import argv

if __name__ == "__main":
    total = 0

    for arg in argv[1:]:
        total += int(arg)

    print(total)
