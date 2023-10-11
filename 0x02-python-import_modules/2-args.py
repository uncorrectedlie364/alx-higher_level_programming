#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_arguments = len(argv) - 1  # Subtract 1 to exclude the script name

    if num_arguments == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        print("Number of argument(s):", num_arguments)
        print("Arguments:", end=' ')
        if num_arguments == 1:
            print(":", end='\n')
        else:
            print("s:", end='\n')

        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}")
