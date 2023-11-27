#!/usr/bin/python3
"""create a square"""


class Square:
    """init one"""
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    """calc the area"""
    def area(self):
        return (self.__size * self.__size)

    @sizeset
    """set the value"""
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @sizereturn
    """return the value"""
    def size(self):
        return self.__size
