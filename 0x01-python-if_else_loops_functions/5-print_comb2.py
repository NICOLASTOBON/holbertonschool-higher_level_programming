#!/usr/bin/python3
for idx in range(0, 100):
    if idx != 99:
        print("{:d}".format(idx).zfill(2), end=', ')
    else:
        print("{:d}".format(idx))
