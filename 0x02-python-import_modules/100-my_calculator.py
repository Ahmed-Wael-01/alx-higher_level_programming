#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    av = sys.argv
    if len(av) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(av[1)]
    b = int(av[3])
    op = av[2]
    if op == "+":
        print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b)))
    elif op == "-":
        print("{:d} {} {:d} = {:d}".format(a, op, b, sub(a, b)))
    elif op == "*":
        print("{:d} {} {:d} = {:d}".format(a, op, b, mul(a, b)))
    elif op == "/":
        print("{:d} {} {:d} = {:d}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
