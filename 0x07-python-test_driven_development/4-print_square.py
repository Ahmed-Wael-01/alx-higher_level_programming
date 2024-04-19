#!/usr/bin/python3
"""printing squares"""


def print_square(size):
    """prints a square with the entered size using # symbole"""
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/4-print_square.txt")
