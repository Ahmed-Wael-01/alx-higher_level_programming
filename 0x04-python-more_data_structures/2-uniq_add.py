#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    add = 0
    map(lambda x: add += x, new)
    return add
