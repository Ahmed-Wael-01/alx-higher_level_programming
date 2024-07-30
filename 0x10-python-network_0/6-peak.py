#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds peak
    """
    lt = 0
    rt = len(list_of_integers) - 1
    while lt <= rt:
        m = lt + ((rt - 1) // 2)
        if m > 0 and list_of_integers[m] < list_of_integers[m - 1]:
            rt = m - 1
        elif m < len(list_of_integers) - 1 and\
        list_of_integers[m] < list_of_integers[m + 1]:
            lt = m + 1
        else:
            return list_of_integers[m]
