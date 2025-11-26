#!/usr/bin/python3
''' Task 13. Can I? '''


def add_attribute(obj, name, value):
    ''' Add a new attribute to an object if possible.
        Write a function that adds a new attribute to
        an object if it's possible:
        Raise a TypeError exception, with the message can't add
        new attribute if the object can't have new attribute
        You are not allowed to use try/except
    '''

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
