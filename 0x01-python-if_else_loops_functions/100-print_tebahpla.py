#!/usr/bin/python3
for x in range(122, 96, -1):
    if x % 2 == 0:
        alpha = x
    else:
        alpha = x - 32
    print("{:c}".format(alpha), end='')
