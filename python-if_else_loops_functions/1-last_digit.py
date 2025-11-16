#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = -(10 - last_digit)
if last_digit > 5:
    str1 = "greater than 5"
elif last_digit == 0:
    str1 = "0"
else:
    str1 = "less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} and is {str1}")
