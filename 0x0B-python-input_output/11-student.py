#!/usr/bin/python3
"""student to json?!!"""


class Student():
    """creates students"""
    def __init__(self, first_name, last_name, age):
        """init a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns json"""
        if type(attrs) is not list:
            return self.__dict__
        for x in attrs:
            if type(x) is not str:
                return self.__dict__
        new_dict = dict()
        for key, val in self.__dict__.items():
            if key in attrs:
                new_dict[key] = val
        return new_dict

    def reload_from_json(self, json):
        """replace attributes"""
        if len(json) == 0:
            return
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
