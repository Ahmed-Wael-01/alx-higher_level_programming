#!/usr/bin/python3
"""checks the subclass"""


def inherits_from(obj, a_class):
    """checks something i guess"""
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
