#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """making rectangle objects"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """makes a new rectangle"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """sets the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """sets x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """sets y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def display(self):
        """it displays the rectangle in high quality"""
        print('\n' * self.__y, end='')
        for x in range(self.__height):
            print(' ' * self.__x, end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """updates values of the rectangle"""
        if not args:
            if "id" in kwargs:
                self.__id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
        elif args and len(args) > 0:
            if len(args) >= 1:
                self.__id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]

    def to_dictionary(self):
        """returns dict"""
        return {'x': self.__x, 'y': self.__y,
                'id': self.__id, 'height': self.__height,
                'width': self.__width}

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
