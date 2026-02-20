#!/usr/bin/python3
"""
This module has the Square class with checks for size.
"""


class Square:
    """Represents a square and makes sure the size is valid.
    
    Attributes:
        __size (int): The size of the square
    """
    
    def __init__(self, size=0):
        """Create a new Square and check the size is okay.
        
        Args:
            size (int): the size for the square, default is 0
            
        Raises:
            TypeError: If size isn't an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size