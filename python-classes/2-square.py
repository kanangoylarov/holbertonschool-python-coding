#!/usr/bin/python3
"""square class
"""


class Square:
    """square size class error
    """
    __size = 0

    def __init__(self, size=0):
        """class rewiews
        """
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area of square"""

        return self.__size * self.__size
