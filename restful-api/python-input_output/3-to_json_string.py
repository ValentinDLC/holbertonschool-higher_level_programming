#!/usr/bin/python3
"""Module that converts a Python object to a JSON string (output operation)"""

import json

def to_json_string(my_obj):
    """Converts a python object into its JSON sreing representation"""
    return json.dumps(my_obj)