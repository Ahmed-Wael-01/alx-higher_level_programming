#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    return (sum(x * z for x, z in my_list) / sum(z for x, z in my_list))
