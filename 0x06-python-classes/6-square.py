#!/usr/bin/python3
"""Square class"""


class Square():
    """constuctor method"""

    def __init__(self, size=0, position=(0, 0)):
        """private attribute"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """using property decorator"""

        return self.__position

    @position.setter
    def position(self, value):
        """Setter and value validation"""

        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """ prints in stdout the square with the character # """

        num = self.size
        line = self.position

        if num == 0:
            print("")
        else:
            for _ in range(line[1]):
                print("")
            for _ in range(num):
                for j in range(num + line[0]):
                    if j < line[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print("")
