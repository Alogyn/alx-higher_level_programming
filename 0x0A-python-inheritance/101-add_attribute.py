#!/usr/bin/python3
'''
Module for add_attribute function.
'''


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible.

    Raises a TypeError exception if the object can't have a new attribute.

    Args:
        obj (object): The object to which the attribute should be added.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
