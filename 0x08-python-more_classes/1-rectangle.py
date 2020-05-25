#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Initial method """

    def __init__(self, width=0, height=0):
        """ defines a rectangle """

        self.width = width
        self.height = height

    @property
    def width(self):
        """using property decorator"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter and value validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """using property decorator"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter and value validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
