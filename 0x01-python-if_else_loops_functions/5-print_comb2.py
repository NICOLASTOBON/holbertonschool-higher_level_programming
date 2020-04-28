#!/usr/bin/python3
for idx in range(0, 100):
    if idx != 99:
        print("{:02d}".format(idx), end=', ')
    else:
        print("{:d}".format(idx))
