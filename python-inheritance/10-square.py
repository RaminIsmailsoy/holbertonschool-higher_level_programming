#!/usr/bin/python3
''' Task 10.  Square #1 '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' 
    Rectangle is the parent (superclass) of Square  
    Square is a subclass (child) of Rectangle
    Square automatically gets all methods and attributes of Rectangle
    '''

    def __init__(self, size):
        ''' Initialize a new square.
        Argsuments are:
            size (int): The size of the new square.
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
