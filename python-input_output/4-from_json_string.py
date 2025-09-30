#!/usr/bin/python3
"""Module that converts a JSON string to object"""

import json

def from_json_string(my_str):
    """
    Returns an object (python data structure) represented by a JSON string

        Input: A JSON formatted string
        Outpout: The equivalent python data structure
    """
    return json.loads(my_str)