#!/usr/bin/env python3
"""
CSV to JSON conversion module.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and save to data.json.
    
    Args:
        csv_filename: The name of the CSV file to convert
        
    Returns:
        True if conversion was successful, False otherwise
    """
    try:
        # Read CSV file and convert to list of dictionaries
        data = []
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        # Write to JSON file
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    
    except FileNotFoundError:
        return False
    except Exception:
        return False