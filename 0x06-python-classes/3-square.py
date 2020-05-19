#!/usr/bin/python3
"""Square class"""


class Square():
    """constuctor method"""

    def __init__(self, size=0):
        """Size validation"""

        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of a square"""

        return self.__size ** 2
