#!/usr/bin/python3
"""
Module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div

    Args:
        matrix (list of lists): matrix of integers or floats
        div (int or float): divisor

    Returns:
        list of lists: new matrix with divided values

    Raises:
        TypeError: if matrix is not a list of lists of numbers
        TypeError: if rows of matrix are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Validate matrix structure
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(error_msg)
        for num in row:
            if not isinstance(num, (int, float)) or isinstance(num, bool):
                raise TypeError(error_msg)

    # Validate row sizes
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div (check bool is subclass of int)
    if isinstance(div, bool) or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for NaN and infinity
    if div != div or div == float('inf') or div == float('-inf'):
        raise TypeError("div must be a number")

    # Check division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide matrix
    return [[round(num / div, 2) for num in row] for row in matrix]
