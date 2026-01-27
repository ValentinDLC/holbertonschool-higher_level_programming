#!/usr/bin/python3
"""
Defines a Sqaure class with size validation
"""
class square:
    """
    reprensents always a square fort this project
    """
    def __init__(self, size=0):
        """
        Initialize a square with a given size

        Args:
            size(int): Size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance (size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        
        self.__size = size
