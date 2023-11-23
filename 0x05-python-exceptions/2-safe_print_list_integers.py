#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        while num < x:
            if type(my_list[num]) is int:
                print("{:d}".format(my_list[num]), end='')
            num += 1
    except IndexError:
        None
    print()
    return num
