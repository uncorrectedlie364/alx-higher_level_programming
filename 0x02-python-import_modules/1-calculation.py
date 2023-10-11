#!/usr/bin/python3

if __name__ == "__main__":
# Print the sum, difference, product, and quotient of 10 and 5.

# Import functions from calculator_1.py
    from calculator_1 import add, sub, mul, div

# Define the numbers
    a = 10
    b = 5

# Calculate and print the results
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
