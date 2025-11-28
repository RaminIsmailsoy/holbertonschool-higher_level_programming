#!/usr/bin/python3

''' 11. Student to disk and reload
Write a class Student that defines a student by: (based on 10-student.py)
'''


class Student:

    ''' This is a class name. '''

    def __init__(self, first_name, last_name, age):

        ''' Initilize a new class '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        ''' A mwthod named to_jason '''

        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):

        ''' Replace all attributes of the Student '''

        for k, v in json.items():
            setattr(self, k, v)
