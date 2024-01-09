#!/usr/bin/python3
"""
Module for append_write function.
"""

def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
    return len(text)

if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
