#!/usr/bin/python3
""" Class """


class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """ Initial variable """
        self.first_name = first_name
