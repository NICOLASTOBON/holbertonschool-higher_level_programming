#!/usr/bin/python3
def uppercase(str):
    str_upper = []
    for idx in range(len(str)):
        if ord('a') <= ord(str[idx]) <= ord('z'):
            str_upper.append(chr(ord(str[idx]) - 32))
        else:
            str_upper.append(str[idx])

    print("{}".format(''.join(str_upper)))
