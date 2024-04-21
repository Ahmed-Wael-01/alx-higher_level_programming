#!/usr/bin/python3
"""improved geometry class"""


class BaseGeometry():
    """raise exception in area"""
    def area(self):
        """it's still under work"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates information"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry)
    """simple rectangle class"""
    def __init__(self, width, height):
        """initializes the rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
