#!/usr/bin/python3
"""
Module 4-print_square
Prints a square with character #
"""


def print_square(size):
    """
    Prints a square with '#'

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not an int
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
        