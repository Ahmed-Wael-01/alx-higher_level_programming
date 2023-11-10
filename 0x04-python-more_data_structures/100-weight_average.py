#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0
    return (sum(x * z for x, z in my_list) / sum(z for x, z in my_list))
