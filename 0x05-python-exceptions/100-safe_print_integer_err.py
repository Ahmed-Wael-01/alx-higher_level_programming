#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    flage = True
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception:", error, file=sys.stderr)
        flage = False
    return flage
