#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else -(abs(number) % 10)

if last_digit > 5:
    desc = "and is greater than 5"
elif last_digit == 0:
    desc = "and is 0"
else:
    desc = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {desc}")
