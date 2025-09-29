#!/usr/bin/python3
"""
Module that appends a string to a text file (output operation)
"""

def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8)."""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
    