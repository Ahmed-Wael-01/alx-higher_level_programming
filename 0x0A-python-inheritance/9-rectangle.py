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

    def area():
        """calc area"""
        return __width * __height

    def print():
        """prints something"""
        print("[Rectangle] {}/{}".format(__width, __height))

    def str():
        """returns something"""
        return "[Rectangle] {}/{}".format(__width, __height)
