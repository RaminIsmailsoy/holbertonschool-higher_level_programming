#!/usr/bin/python3
'''MyInt module'''


class MyInt(int):
    '''MyInt is a rebel: == and != are inverted'''

    def __eq__(self, other):
        '''Invert equality'''
        return not super().__eq__(other)

    def __ne__(self, other):
        '''Invert inequality'''
        return not super().__ne__(other)

