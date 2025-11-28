#!/usr/bin/python3

''' Task 10. Student to JSON with filter
Write a class Student that defines a student by: (based on 9-student.py)
'''


class Student:

    ''' This is a class. We call it Student '''

    def __init__(self, first_name, last_name, age):

        ''' Initialize Student class '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        ''' This is a method '''

        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
