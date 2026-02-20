#!/usr/bin/python3
"""Module that defines a student class with filtered JSON"""

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved. Otherwise, all attributes are retrieved.
        """
        if attrs is None:
            return self.__dict__
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
