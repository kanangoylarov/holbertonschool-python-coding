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

    @property
    def size(self):
        """getter of size"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter of value"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """square pritner with hasbangs"""

        if self.__size == 0:
            print("")
        else:
            i = 0
            while (i < self.__size):
                j = 0
                while(j < self.__size):
                    print("#",end="")
                    j += 1
                print()
                i += 1
                    
