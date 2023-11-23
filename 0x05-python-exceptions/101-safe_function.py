#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        rtrn = fct(*args)
        return rtrn
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
