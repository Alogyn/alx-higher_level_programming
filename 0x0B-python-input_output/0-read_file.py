#!/usr/bin/python3
'''
Module for read_file function.
'''


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
