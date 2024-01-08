#!/usr/bin/python3
'''
Module for print_sorted function.
'''


class MyList(list):
    """
    MyList class that inherits from list.

    Public instance method:
    - def print_sorted(self): Prints the list, but sorted (ascending sort).

    """

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
