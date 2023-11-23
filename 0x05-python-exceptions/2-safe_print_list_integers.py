#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    while num < x:
        try:
            if type(my_list[num]) is int:
                print("{:d}".format(my_list[num]), end='')
        except IndexError:
            None
        num += 1
    return num
