#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("")
        return
    for x in range(len(matrix)):
        for z in range(len(matrix[x])):
            print("{:d}".format(matrix[x][z]), end='')
            if z != len(matrix[x]) - 1:
                print(" ", end='')
        print("")
