#!/usr/bin/python3
"""rectangle class"""
from  models.base import Base


class Rectangle(Base):
    """making rectangle objects"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """makes a new rectangle"""
        super().__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @proberty
    def width(self):
        """gets the width"""
        return __width

    @proberty
    def height(self):
        """gets the height"""
        return __height

    @proberty
    def x(self):
        """gets x"""
        return __x

    @proberty
    def y(self):
        """gets y"""
        return __y

    @width.setter
    def width(self, width):
        """sets the width"""
        self.__width = width

    @height.setter
    def height(self, height):
        """sets the height"""
        self.__height = height

    @x.setter
    def x(self, x):
        """sets x"""
        self.__x = x

    @y.setter
    def y(self, y):
        """sets y"""
        self.__y = y
