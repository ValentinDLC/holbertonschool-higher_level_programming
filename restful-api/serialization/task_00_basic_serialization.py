#!/usr/bin/env python3
"""
Basic serialization module for converting Python dictionaries to/from JSON files.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    
    Args:
        data: A Python dictionary with data to serialize
        filename: The filename of the output JSON file (will be replaced if exists)
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.
    
    Args:
        filename: The filename of the input JSON file
        
    Returns:
        A Python dictionary with the deserialized JSON data
    """
    with open(filename, 'r') as f:
        return json.load(f)