#!/usr/bin/python3
"""
Module for save_to_json_file function.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using a JSON representation.

    Args:
        my_obj (object): The Python object to be saved.
        filename (str): The name of the file to write.

    Returns:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
