#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = sys.argv
    sum = 0
    for x in range(1, len(av)):
        sum += int(av[x])
    print("{:d}".format(sum))
