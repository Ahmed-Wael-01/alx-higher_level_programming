#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            print("{:c}".format(ord(x) - 32), end='')
        else:
            print(x, end='')
