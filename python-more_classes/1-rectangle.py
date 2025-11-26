#!/usr/bin/python3
""" Real definition of a rectangle """


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for __width."""
        return self.__width

    @property
    def height(self):
        """Getter for __height."""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
