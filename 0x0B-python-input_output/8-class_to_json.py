#!/usr/bin/python3
"""
Module for class_to_json function.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: Dictionary representation of the object.
    """
    # Get the dictionary representation of the object's __dict__
    return obj.__dict__
