#!/usr/bin/env python3
"""
Custom class serialization using pickle module.
"""
import pickle


class CustomObject:
    """
    A custom class with serialization capabilities using pickle.
    
    Attributes:
        name (str): The person's name
        age (int): The person's age
        is_student (bool): Whether the person is a student
    """
    
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.
        
        Args:
            name: A string representing the name
            age: An integer representing the age
            is_student: A boolean indicating student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """
        Display the object's attributes in a formatted manner.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.
        
        Args:
            filename: The name of the file to save the serialized object
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None
    
    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.
        
        Args:
            filename: The name of the file containing the serialized object
            
        Returns:
            An instance of CustomObject, or None if an error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, Exception):
            return None