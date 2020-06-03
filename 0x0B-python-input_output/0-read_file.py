#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """ Read a file """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
    f.close()
