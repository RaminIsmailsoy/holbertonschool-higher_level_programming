#!/usr/bin/python3
''' Task 9. Student to JSON
Write a class Student that defines a student by:
Public instance attributes: first_name, last_name, age
'''


class Student:

    ''' Defines a new class called Student.
    A class is a blueprint for creating objects. '''

    def __init__(self, first_name, last_name, age):

        ''' Initialize Student class '''
        ''' Method is automatically called when a new Student object is created'''
        ''' self refers to the current object being created .'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        ''' to_json is a method that returns a dictionary of the object'''
        ''' It can be converted to JSON. '''

        return self.__dict__
