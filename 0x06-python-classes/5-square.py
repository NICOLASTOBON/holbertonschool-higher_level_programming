#!/usr/bin/python3
"""Square class"""


class Square():
    """constuctor method"""

    def __init__(self, size=0):
        """private attribute"""

        self.__size = size

    def area(self):
        """Area of a square"""

        return self.__size ** 2

    @property
    def size(self):
        """using property decorator"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter and value validation"""

        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ prints in stdout the square with the character # """

        num = self.__size

        if num is 0:
            print("")
        else:
            for _ in range(num):
                for _ in range(num):
                    print("#", end='')
                print("")
