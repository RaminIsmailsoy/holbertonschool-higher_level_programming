#!/usr/bin/python3

"""
Task 1. Pickling Custom Classes
Learn how to serialize and deserialize custom Python objects using the pickle module.
1 - Create a custom Python class named CustomObject.
This class should have the following attributes:
2 - Implement two methods within this class:
3 - Save your code in a file named task_01_pickle.py
"""


import json


def serialize_and_save_to_file(data, filename):
    """Function serializes data to JSON
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Function desirializes JSON data into python dictionery """

    with open(filename, "r", encoding="utf-8") as f:
        dictionery = json.load(f)
    return dictionery
