#!/usr/bin/python3
import sys

if __name__ == '__main__':
    i = 1
    sum_argv = 0
    len_argv = len(sys.argv)
    if len_argv is 1:
        print("0")
    else:
        while (i < len_argv):
            sum_argv += int(sys.argv[i])
            i += 1
        print("{:d}".format(sum_argv))
