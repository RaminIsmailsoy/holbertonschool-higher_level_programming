#!/usr/bin/python3

''' Task 6. Write a function that creates an Object from a JSON file '''


from json import loads

''' Imports the loads function from the json module.
loads function is used for deserialization.
Converting a JSON string back into a Python object '''


def load_from_json_file(filename):

    ''' Define a function called load_from_json_file '''

    with open(filename, encoding='utf-8') as f:

        ''' Read the entire JSON string content from the file '''
        return loads(f.read())
