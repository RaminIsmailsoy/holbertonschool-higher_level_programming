#!/usr/bin/python3
""" MyList class """


class MyList(list):
    """ Create MyList class """

    def print_sorted(self):
        """Print a list in sorted order"""
        print(sorted(self))
