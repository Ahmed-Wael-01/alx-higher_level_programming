#!/usr/bin/python3
"""create squares"""


class Square:
    """class that makes squares"""
    def __init__(self, size=0, position=(0, 0)):
        """init one"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        if (type(position) != tuple or len(position) != 2 or
                type(position[0]) != int or type(position[1]) != int or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
