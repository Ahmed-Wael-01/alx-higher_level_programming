#!/usr/bin/python3
"""read!!!!"""


def read_file(filename=""):
    """reading files all day long"""
    with open("filename", encoding="utf-8") as fl:
        text = fl.read()
        print(text)
