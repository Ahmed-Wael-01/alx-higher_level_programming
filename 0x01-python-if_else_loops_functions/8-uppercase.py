#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            alpha = ord(x) - 32
        else:
            alpha = ord(x)
        print("{:c}".format(alpha), end='')
    print("")
