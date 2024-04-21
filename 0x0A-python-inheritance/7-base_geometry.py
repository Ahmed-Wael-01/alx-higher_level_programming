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
