#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuble_a) > 1:
        a1 = tuble_a[0]
        a2 = tuble_a[1]
    elif len(tuble_a) > 0:
        a1 = tuble_a[0]
        a2 = 0
    else:
        a1 = 0
        a2 = 0
    if len(tuble_b) > 1:
        b1 = tuble_b[0]
        b2 = tuble_b[1]
    elif len(tuble_b) > 0:
        b1 = tuble_b[0]
        b2 = 0
    else:
        b1 = 0
        b2 = 0
    return (a1 + b1, a2 + b2)
