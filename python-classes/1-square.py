#!/usr/bin/python3
"""square class
"""


class Square:
    """square size class error
    """
    __size = 0

    def __init__(self, size):
        """class rewiews
        """
        self.__size = size
        if type(self.size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
