#!/usr/bin/python3
"""simple square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """making a cute square"""
    def __init__(self, size):
        """init a square"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """calc area"""
        return self.__size ** 2
