#!/usr/bin/python3
"""Square module

 This module contains the Square class.
 """

class Square:
    """A class that define a square.
    
    Attributes:
        __size (int): The size of the private square.
    """

    def __init__(self, size):
        """Initialize a new Square.
        
        Args:
           size: The size of the new square.
        """
        self.__size = size