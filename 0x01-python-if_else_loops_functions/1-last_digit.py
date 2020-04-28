#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    num = number % 10
else:
    num = (abs(number) % 10) * -1

str_num = "Last digit of {:d}".format(number)

if num > 5:
    print("{} is {:d} and is greater than 5".format(str_num, num))
elif 6 > num != 0:
    print("{} is {:d} and is less than 6 and not 0".format(str_num, num))
else:
    print("{} is {:d} and is 0".format(str_num, num))
