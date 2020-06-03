#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """ Read a file """
    with open("my_file_0.txt", encoding="utf-8") as f:
        print(f.read())
    f.close()
