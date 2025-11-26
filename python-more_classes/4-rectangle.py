#!/usr/bin/python3
"""Eval is magic"""


class Rectangle:
    """Class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width with type and value checks"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height with type and value checks"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Return a string representation of the rectangle using '#'"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Return a string that can recreate this rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
