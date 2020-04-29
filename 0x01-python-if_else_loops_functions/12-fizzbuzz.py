#!/usr/bin/python3
def fizzbuzz():
    for idx in range(1, 101):
        if (idx % 3) is 0 and (idx % 5) is 0:
            print("FizzBuzz", end=' ')
        elif ((idx % 3) is 0) and (not (idx % 5) is 0):
            print("Fizz", end=' ')
        elif ((idx % 5) is 0) and (not (idx % 3) is 0):
            print("Buzz", end=' ')
        else:
            print("{}".format(idx), end=' ')
