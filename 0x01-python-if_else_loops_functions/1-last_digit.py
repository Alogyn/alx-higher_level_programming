#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 9:
    last_digit = number % 10
else:
    last_digit = number

if last_digit < 6:
    print(f"Last digit of {number:d} is {last_digit:d}", end=' ')
    print("and is less than 6 and not 0")
elif last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} greater than 5")
else:
    print(f"Last digit of {number:d} is {last_digit:d} 0")
