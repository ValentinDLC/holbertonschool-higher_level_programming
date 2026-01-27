#!/usr/bin/python3
"""
Defines a Rectangle class with width and height
"""


class Rectangle:
    """
    Represents a rectangle
    """
    def __init__(self, widht=0, height=0):
        """
        Initialize a new Rectangle instance

        Args:
            width (int): Width of the rectangle (default is 0)
            height (int): Height of the rectangle (default is 0)
        """
        self.width = widht
        self.height = height

    @property
    def widht(self):
        """
        Get the width of the rectangle

        Returns:
            int: Width of the rectangle
        """
        return self.__widht

    @widht.setter
    def widht(self, value):
        """
        Set the width of the rectangle

        Args:
            value (int): The new width

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__widht = value

    @property
    def height(self):
        """
        Get the height of the rectangle

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        Args:
            value (int): The new height
        """
        if not isinstance:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
