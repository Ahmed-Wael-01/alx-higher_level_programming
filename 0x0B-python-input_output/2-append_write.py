#!/usr/bin/python3
"""documentaion is awesome"""


def append_write(filename="", text=""):
    """i'm sure it does something"""
    with open(filename, "a", encoding="utf-8") as ofile:
        return ofile.write(text)
