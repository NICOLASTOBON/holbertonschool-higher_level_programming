#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    op = ['+', '-', '*', '/']
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = sys.argv[1]
        c = sys.argv[2]
        b = sys.argv[3]
        if c in op:
            if c is op[0]:
                print("{} {} {} = {}".format(a, op[0], b, add(int(a), int(b))))
            elif c is op[1]:
                print("{} {} {} = {}".format(a, op[1], b, sub(int(a), int(b))))
            elif c is op[2]:
                print("{} {} {} = {}".format(a, op[2], b, mul(int(a), int(b))))
            else:
                print("{} {} {} = {}".format(a, op[3], b, div(int(a), int(b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
