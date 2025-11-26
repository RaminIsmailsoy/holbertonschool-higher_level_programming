#!/usr/bin/python3
""" A module with a Rectangle that does nothing """


class Rectangle:
    """  An empty Rectangle class  """

    def __init__(self, width=0, height=0):
       
       """   Checks the parameters and initializes some values. """

        self.__check_valid_width(width)
        self.__check_valid_height(height)

        self.width = width
        self.height = height

    @property
    def width(self):
        """       Returns the width of the Rectangle      """

        return self.__width

    @width.setter
    def width(self, value):
        """     Checks the parameters and set the size of the Rectangle """

        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self):
        """        Returns the width of the Rectangle      """

        return self.__height

    @height.setter
    def height(self, value):
        """      Checks the parameters and set the size of the Rectangle"""
        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width):
        """        Checks if the width is a valid integer"""

        if self.__check_int_value(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive_value(width) is False:
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height):
        """        Checks if the height is a valid integer"""

        if self.__check_int_value(height) is False:
            raise TypeError('height must be an integer')

        if self.__check_positive_value(height) is False:
            raise ValueError('height must be >= 0')

    def __check_int_value(self, value):
        
        """        Checks if the value is an integer"""

        if type(value) is int:
            return True

        return False

    def __check_positive_value(self, value):
        """       Checks if the value is a positive intege"""

        if value >= 0:
            return True

        return False
