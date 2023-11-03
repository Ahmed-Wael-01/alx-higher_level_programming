#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = sys.argv
    if len(av) - 1 == 0:
        print("0 arguments.")
    elif len(av) - 1 == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(av) - 1))
    for x in range(len(av) - 1):
        print("{:d}: {}".format(x + 1, av[x + 1]))
