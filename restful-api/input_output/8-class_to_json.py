#!/usr/bin/python3
"""Module that returns the dictionary description for JSON serialization """

def class_to_json(obj):
    """Returns the dictionary description with simple data structure for JSON serialization"""
    return obj.__dict__