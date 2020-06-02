#!/usr/bin/python3
""" Class Mylist"""


class MyList(list):
    """ Mylist """

    def print_sorted(self):
        """ prints the list sorted """
        print(sorted(self))
