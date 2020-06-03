#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """ Read a file """
    with open("my_file_0.txt", 'r') as f:
        line = f.read()
    print(line, end="")
