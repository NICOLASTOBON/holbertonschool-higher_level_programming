#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = sys.argv[1]
        c = sys.argv[2]
        b = sys.argv[3]
        if c is '+':
            print("{} + {} = {}".format(a, b, add(int(a), int(b))))
        elif c is '-':
            print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
        elif c is '*':
            print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
        elif c is '/':
            print("{} / {} = {}".format(a, b, div(int(a), int(b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
