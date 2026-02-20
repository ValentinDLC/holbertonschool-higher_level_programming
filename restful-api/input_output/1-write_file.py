#!/usr/bin/python3
"""
Module that writes a string to a text file (output operation)
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8).

        Input: The string provided by user/program
        Outpout : The string stored inside the file
        Returns: Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
