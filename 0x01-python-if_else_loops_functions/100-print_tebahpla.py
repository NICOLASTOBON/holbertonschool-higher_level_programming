#!/usr/bin/python3
for idx in range(90, 64, -1):
    if idx % 2 == 0:
        idx += 32
    print("{}".format(chr(idx)), end='')
