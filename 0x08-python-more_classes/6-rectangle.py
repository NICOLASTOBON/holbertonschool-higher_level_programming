#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Initial method """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ defines a rectangle """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ print the rectangle """
        if self.__height == 0 or self.__width == 0:
            return ""
        str_new = ('#' * self.__width + '\n') * self.__height
        return str_new.strip('\n')

    def __repr__(self):
        """ print Rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ print the message Rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """ Area Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter Rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            p = 2 * (self.__height + self.__width)
            return p
