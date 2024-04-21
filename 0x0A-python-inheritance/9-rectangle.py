#!/usr/bin/python3
"""improved geometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """simple rectangle class"""
    def __init__(self, width, height):
        """initializes the rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calc area"""
        return self.__width * self.__height

    def __str__(self):
        """description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
