#!/usr/bin/python3
"""Module that creates a Python object from a JSON file"""

import json

def load_from_json_file(filename):
    """Reads a JSON file and deserializes it into a Python object."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
    