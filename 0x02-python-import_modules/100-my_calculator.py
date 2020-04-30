#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    op = ['+', '-', '*', '/']
    len_argv = len(sys.argv) - 1
    if len_argv != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    else:
        a = sys.argv[1]
        c = sys.argv[2]
        b = sys.argv[3]
        if c is op[0]:
            print("{} {} {} = {}".format(a, op[0], b, add(int(a), int(b))))
        elif c is op[1]:
            print("{} {} {} = {}".format(a, op[1], b, sub(int(a), int(b))))
        elif c is op[2]:
            print("{} {} {} = {}".format(a, op[2], b, mul(int(a), int(b))))
        elif c is op[3]:
            print("{} {} {} = {}".format(a, op[3], b, div(int(a), int(b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
