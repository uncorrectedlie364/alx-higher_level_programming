#!/usr/bin/python3
for number in range(99):
    formatted_number = "{:02}".format(number)
    print("{}, ".format(formatted_number), end="")
print("99")
