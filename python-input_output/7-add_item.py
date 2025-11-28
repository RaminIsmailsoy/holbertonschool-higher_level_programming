#!/usr/bin/python3
''' Task 7. Write a script that adds all arguments to a Python list, and then save them to a file '''


from os import path
''' The Operating System interface module. It provides a way of interacting with the operating system.
Things like reading or writing files, creating directories, and handling environment variables.'''

from sys import argv
''' The System module. It provides access to system-specific parameters and functions '''

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.exists('add_item.json'):
    obj_json_file = load_from_json_file('add_item.json')
else:
    obj_json_file = []

for i in range(1, len(argv)):
    obj_json_file.append(argv[i])

save_to_json_file(obj_json_file, 'add_item.json')
