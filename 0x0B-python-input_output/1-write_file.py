#!/usr/bin/python3
'''
Module for write_file function.
'''


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
