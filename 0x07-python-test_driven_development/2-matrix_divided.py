#!/usr/bin/python3
"""
module for dividing all matrix elements
"""


def matrix_divided(matrix, div):

    """
    Returns new matix divided by div to two d.p
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:

        raise TypeError(msg)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)
    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
