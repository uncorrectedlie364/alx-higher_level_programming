#!/usr/bin/python3

# Import add and assign it to a different name (e.g., my_add)
from add_0 import add as my_add

a = 1
b = 2

# Calculate the result using the add function
result = my_add(a, b)

# Print the result with string formatting
print("{} + {} = {}".format(a, b, result))
