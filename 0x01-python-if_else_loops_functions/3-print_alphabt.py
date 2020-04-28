#!/usr/bin/python3
for idx in range(97, 123):
    if idx != ord('e') and idx != ord('q'):
        print("{:s}".format(chr(idx)), end='')
