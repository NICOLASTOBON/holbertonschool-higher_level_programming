#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:

    def area(self):
        """ Public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validator integer """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


""" class Rectangle """


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """ initial attributes """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
