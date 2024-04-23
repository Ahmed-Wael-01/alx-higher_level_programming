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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """updates values of the rectangle"""
        if not args:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.__width = kwargs["size"]
                self.__height = kwargs["size"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
        elif args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
                self.__height = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]

    def __str__(self):
        """description of square"""
        "[Square] ({}) {}/{} - {}".format(
                self.id, self.__x, self.__y, self.__width)
