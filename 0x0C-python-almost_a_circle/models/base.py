#!/usr/bin/python3
"""base class file"""
import json


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

    def to_json_string(list_dictionaries):
        """returns json"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json"""
        if list_objs is not None:
            list_objs = [x.to_dictionary() for x in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))
