#!/usr/bin/python3
"""squares everywhere"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """making a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets size"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets size"""
        self.width = value
        self.height = value

    def __str__(self):
        """description of square"""
        "[Square] ({}) {}/{} - {}".format(
                self.__id, self.__x, self.__y, self.__width)