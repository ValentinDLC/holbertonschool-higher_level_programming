#!/usr/bin/python3
"""Class that defines a square with size and position."""


class Square:
    """A square with size checks and position coordinates."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Create a square and check size and position.
        
        Args:
            size (int): The side length of the square (default: 0)
            position (tuple): The (x, y) offset for printing (default: (0, 0))
        """
        self.size = size
        self.position = position
    
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
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """Return the position of the square.
        
        Returns:
            tuple: The (x, y) offset
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """Update the position of the square and check if it’s valid.
        
        Args:
            value (tuple): The new (x, y) offset
            
        Raises:
            TypeError: If it’s not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """Return the area of the square.
        
        Returns:
            int: The area (side × side)
        """
        return self.__size ** 2
    
    def my_print(self):
        """Print the square using '#' with position offsets.
        
        If size is 0, print an empty line.
        position[0] = spaces before each line.
        position[1] = empty lines before the square.
        """
        if self.__size == 0:
            print()
        else:
            # Print vertical offset
            for _ in range(self.__position[1]):
                print()
            
            # Print square with horizontal offset
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
