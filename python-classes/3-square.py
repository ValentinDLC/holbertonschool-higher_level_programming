#!/usr/bin/python3
"""Class that defines a square and checks its size."""


class Square:
    """A square with a given size."""
    
    def __init__(self, size=0):
        """Create a square and check if the size is valid.
        
        Args:
            size (int): The length of the square's side (default: 0)
            
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Return the area of the square.
        
        Returns:
            int: The area (side × side)
        """
        return self.__size ** 2
