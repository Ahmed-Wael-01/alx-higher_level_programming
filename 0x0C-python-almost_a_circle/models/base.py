#!/usr/bin/python3
"""base class file"""


class Base:
    """the base and root class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize and setting id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
