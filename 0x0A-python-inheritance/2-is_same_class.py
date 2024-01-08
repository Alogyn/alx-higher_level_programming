#!/usr/bin/python3
'''
Module for is_same_class function.
'''


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if the object is exactly an instance of the specified class;
        otherwise False.

    """
    return type(obj) == a_class
