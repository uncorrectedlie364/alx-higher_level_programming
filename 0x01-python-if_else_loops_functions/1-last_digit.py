#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

# Convert the int to a string
int_str = str(number)

# Extract the last digit as an integer
last_digit = int(int_str[-1])

# Display the last digit with the sign
print("Last digit of", number, "is", int_str[-1], end=" ")

if last_digit < 0:
    last_digit *= -1
    print("and is -", last_digit, "and is less than 6 and not 0")
elif last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
