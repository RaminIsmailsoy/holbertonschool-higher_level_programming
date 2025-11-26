#!/usr/bin/python3
''' Task 9. Full rectangle '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Class name is Rectangle
        BaseGeometry is the parent (or superclass) of Rectangle
        This means Rectangle inherits all methods of BaseGeometry
        Rectangle is a child (subclass) of BaseGeometry
    '''

    def __init__(self, width, height):
        ''' Intialize a new Rectangle.
        Arguments are:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        '''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
