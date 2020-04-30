#!/usr/bin/python3
import sys

if __name__ == '__main__':
    i = 1
    sum_argv = 0
    while (i < len(sys.argv)):
        sum_argv += int(sys.argv[i])
        i += 1
    print("{:d}".format(sum_argv))
