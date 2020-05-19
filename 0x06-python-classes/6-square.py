#!/usr/bin/python3
"""Square class"""


class Square():
    """constuctor method"""

    def __init__(self, size=0, position=(0, 0)):
        """private attribute"""

        self.__size = size
        self.__position = position

    def area(self):
        """Area of a square"""

        return self.__size ** 2

    @property
    def size(self):
        """using property decorator"""

        return self.__size

    @property
    def position(self):
        """using property decorator"""

        return self.__position

    @size.setter
    def size(self, value):
        """Setter and value validation"""

        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Setter and value validation"""

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """ prints in stdout the square with the character # """

        num = self.__size
        line = self.__position

        if num is 0:
            print("")
        else:

            for _ in range(num):
                for j in range(num + line[0]):
                    if (j < line[0]):
                        print(" ", end='')
                    else:
                        print("#", end='')
                print("")
