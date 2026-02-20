#!/usr/bin/python3
"""
This module defines a Rectangle class with width, height, 
instance tracking, custom print symbol, and comparison utilities.
"""


class Rectangle:
    """Rectangle class with width, height, instance tracking, and print symbol."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height.

        Args:
            width (int): Width of the rectangle (default 0)
            height (int): Height of the rectangle (default 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def _validate(self, name, value):
        """Validate that a value is an integer >= 0.

        Args:
            name (str): Name of the attribute
            value (int): Value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0

        Returns:
            int: Validated value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
        return value

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: Width
        """
        return self.__width
    
    @property
    def height(self):
        """Get the height of the rectangle.

       Returns:
            int: Height
        """
        return self.__height
  
    @width.setter
    def width(self, value):
        """Set the width using validation."""
        self.__width = self._validate("width", value)

    @height.setter
    def height(self, value):
        """Set the height using validation."""
        self.__height = self._validate("height", value)

    def area(self):
        """Return the area of the rectangle.

        Returns:
            int: Area (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        Returns:
            int: Perimeter, or 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation using print_symbol.

        Returns:
            str: Rectangle as a string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.__width
                         for _ in range(self.__height))

    def __repr__(self):
        """Return an official string representation of the rectangle.

        Returns:
            str: 'Rectangle(width, height)'
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when a rectangle is deleted and update instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area, or rect_1 if equal.

        Args:
            rect_1 (Rectangle): First rectangle to compare
            rect_2 (Rectangle): Second rectangle to compare

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle

        Returns:
            Rectangle: Rectangle with the larger or equal area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
