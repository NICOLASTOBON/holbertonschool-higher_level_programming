#!/usr/bin/python3
for idx in range(10):
    for jdx in range(idx + 1, 10):
        if idx != 8 or jdx != 9:
            print("{:d}{:d}".format(idx, jdx), end=', ')
        else:
            print("{:d}{:d}".format(idx, jdx))
