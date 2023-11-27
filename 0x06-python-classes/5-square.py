#!/usr/bin/python3
"""create squares"""


class Square:
    """class that makes squares"""
    def __init__(self, size=0):
        """init one"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calc the area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """size of the square.

        Return:
            the value"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size value"""
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if (self.__size is 0):
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print()
