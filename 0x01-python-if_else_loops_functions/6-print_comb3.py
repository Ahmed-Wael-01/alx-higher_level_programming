#!/usr/bin/python3
for x in range(9):
    for i in range(x, 10):
        if x == 8 and i == 9:
            print("{:d}{:d}".format(x, i))
        elif x != i:
            print("{:d}{:d}, ".format(x, i), end='')
