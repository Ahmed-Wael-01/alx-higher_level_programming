#!/usr/bin/python3
"""module to divid matrix by a certain number"""


def matrix_divided(matrix, div):
    """Divides every single element in the matrix by the value of div"""
    if isinstance(matrix, (list)) is False or len(matrix) is 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    new_m = []
    for row in matrix:
        new_r = []
        if isinstance(row, list) is False:
            raise TypeError(
                    "matrix must be a matrix (list of lists)" +
                    " of integers/floats")
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if isinstance(elem, (int, float)) is False:
                raise TypeError(
                        "matrix must be a matrix (list of lists)" +
                        " of integers/floats")
            new_r.append(round(elem / div, 2))
        new_m.append(new_r)
    return new_m


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
