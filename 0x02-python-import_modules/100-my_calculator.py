#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    len_argv = len(sys.argv) - 1
    if len_argv != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
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
            sys.exit(1)
