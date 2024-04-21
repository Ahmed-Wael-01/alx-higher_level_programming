#!/usr/bin/python3
"""some documentation"""


def write_file(filename="", text=""):
    """it does something"""
    with open(filename, "w", encoding="utf-8") as testfile:
        return testfile.write(text)
