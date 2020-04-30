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
        b = sys.argv[2]
        c = sys.argv[3]
        if b in op:
            if b is op[0]:
                print("{} {} {} = {}".format(a, op[0], c, add(int(a), int(c))))
            elif b is op[1]:
                print("{} {} {} = {}".format(a, op[1], c, sub(int(a), int(c))))
            elif b is op[2]:
                print("{} {} {} = {}".format(a, op[2], c, mul(int(a), int(c))))
            else:
                print("{} {} {} = {}".format(a, op[3], c, div(int(a), int(c))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
