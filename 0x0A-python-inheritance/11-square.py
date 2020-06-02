#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

""" Square #1 """


class Square(Rectangle):

    def __init__(self, size):
        """ initial attributes """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()

    def __str__(self):
        """ str """
        return "[Square] {}/{}".format(self.__size, self.__size)
