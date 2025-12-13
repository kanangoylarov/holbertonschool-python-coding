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

        @property
        def size(self):
            """getter of size"""

            return self.__size

        def size(self,value):
            """setter of value"""

            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
