#!/usr/bin/python3
import sys

if __name__ == '__main__':
    i = 1
    len_argv = len(sys.argv)
    if len_argv is 1:
        print("{:d} arguments.".format(len_argv - 1))
    else:
        print("{:d} arguments:".format(len_argv - 1))
        while (i < len_argv):
            print("{:d}: {:s}".format(i, str(sys.argv[i])))
            i += 1
