#!/usr/bin/python3
"""function to say your name"""


def say_my_name(first_name, last_name=""):
    """it print your first and last name"""
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
