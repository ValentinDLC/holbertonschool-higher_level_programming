#!/usr/bin/python3
"""Module that writes a Python object to a text file using JSON"""

import json

def save_to_json_file(my_obj, filename):
    """Serializes a Python object and writes it to a text file as JSON."""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)