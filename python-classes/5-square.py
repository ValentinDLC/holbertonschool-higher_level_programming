#!/usr/bin/python3
"""Class that defines a square and can print it."""


class Square:
    """A square with size checks and print option."""
    
    def __init__(self, size=0):
        """Create a square and check if the size is valid.
        
        Args:
            size (int): The side length of the square (default: 0)
        """
        self.size = size
    
    @property
    def size(self):
        """Return the size of the square.
        
        Returns:
            int: The current size
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Update the size of the square and check if it’s valid.
        
        Args:
            value (int): The new side length
            
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Return the area of the square.
        
        Returns:
            int: The area (side × side)
        """
        return self.__size ** 2
    
    def my_print(self):
        """Print the square using '#' characters.
        
        If size is 0, just print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
