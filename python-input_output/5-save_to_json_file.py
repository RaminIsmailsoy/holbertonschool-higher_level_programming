#!/usr/bin/python3

''' Task 5. Save Object to a file '''


from json import dumps

''' Import the dumps function from Pythons built-in json module.
    dumps() converts a Python object into a JSON-formatted string.'''


def save_to_json_file(my_obj, filename):

    ''' Define a function called save_to_json_file.
    Writes a Python object to a text file using a JSON string representation.'''

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
