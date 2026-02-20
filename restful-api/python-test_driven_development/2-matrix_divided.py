#!/usr/bin/python3
"""
Module 2-matrix_divided
Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int/float): divisor (not zero)

    Returns:
        new_matrix (list of lists): divided matrix

    Raises:
        TypeError: if matrix is not a list of lists of int/float,
                   or if rows have different sizes,
                   or if div is not a number
        ZeroDivisionError: if div == 0
    """
    if not isinstance(matrix, list) or matrix == [] \
       or not all(isinstance(row, list) for row in matrix) \
       or not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
