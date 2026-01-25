#!/usr/bin/python3
"""
Module that provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): first number
        b (int or float): second number (default: 98)

    Raises:
        TypeError: if a or b is not an integer or a float

    Returns:
        int: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN (NaN != NaN is True)
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    # Check for infinity
    if a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
