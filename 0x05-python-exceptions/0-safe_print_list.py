#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    adds = 0
    try:
        while adds < x:
            print(my_list[adds], end='')
            adds += 1
        except IndexError:
            None
        print()
        return adds
