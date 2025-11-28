#!/usr/bin/python3
''' Task 6. Create object from a JSON file '''


from json import loads


def load_from_json_file(filename):
    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
