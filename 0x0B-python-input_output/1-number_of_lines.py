#!/usr/bin/python3
""" Modules """


def number_of_lines(filename=""):
    """ count lines of file """

    line_num = 0
    with open("my_file_0.txt", encoding="utf-8") as f:
        line = f.readlines()
        line_num = len(line)
    f.close()
    return line_num
