#!/usr/bin/python3
"""student to json?!!"""


class Student():
    """creates students"""
    def __init__(self, first_name, last_name, age):
        """init a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns json"""
        return self.__dict__
