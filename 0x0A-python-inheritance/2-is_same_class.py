#!/usr/bin/python3
"""checks originality"""


def is_same_class(obj, a_class):
    """checks if obj is a subclass of a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
