#!/usr/bin/python3
""" Modules """

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initial """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ property """
        return self.__width

    @property
    def height(self):
        """ property """
        return self.__height

    @property
    def x(self):
        """ property """
        return self.__x

    @property
    def y(self):
        """ property """
        return self.__y

    @width.setter
    def width(self, width):
        """ width.setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """ height.setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """ x.setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """ y.setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """ Area """
        return self.__width * self.__height

    def display(self):
        """ Display """
        [print() for _ in range(self.__y)]
        for _ in range(self.__height):
            for j in range(self.__width + self.__x):
                [print(" ", end='') if j < self.__x else print("#", end='')]
            print()

    def update(self, *args, **kwargs):
        """ Update """
        if args:
            attr = ["id", "width", "height", "x", "y"]
            for idx, value in enumerate(args):
                setattr(self, attr[idx], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary """
        new_dict = {}
        for key, value in vars(self).items():
            new_dict[key.split("_")[-1]] = value
        return new_dict

    def __str__(self):
        """ Str """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
            )
