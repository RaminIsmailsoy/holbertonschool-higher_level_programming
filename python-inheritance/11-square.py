#!/usr/bin/python3
''' Task 11. Square #2 '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Class Square that uses Rectangle  '''

    def __init__(self, size):
        ''' Initialize a new square.

        Arguments are:
            size (int): The size of the new square.
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
