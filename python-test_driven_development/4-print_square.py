#!/usr/bin/python3
"""
Defines a function that prints a square with the character #
"""


def print_square(size):
    """
    Prints a square of '#' characters of given size.

    Args:
        size (int): The size of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    # Check if size is a float FIRST (including negative floats)
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    # Check if size is an integer (but not boolean)
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    # Check if size is negative (only after confirming it's an int)
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
