#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """making rectangle objects"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """makes a new rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @property
    def x(self):
        """gets x"""
        return self.__x

    @property
    def y(self):
        """gets y"""
        return self.__y

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
