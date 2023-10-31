#!/usr/bin/python3
"""Defines a string to json function"""
import json


def save_to_json_file(my_obj, filename):
    """write an object a text file JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
