#!/usr/bin/python3
"""my list class to practise inheritance"""


class MyList(list):
    """class that inherits from list class"""
    def print_sorted(self):
        print(sorted(self))
