#!/usr/bin/python3
"""Module for adding integers"""


def add_integer(a, b=98):
    """
    Adds two integers
    
    Args:
        a: first number (integer or float)
        b: second number (integer or float), default is 98
    
    Returns:
        The addition of a and b as integers
    
    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    
    return a + b