#!/usr/bin/python3
"""Defines a string to JASON function"""
import json

def from_json_string(my_str):
    """Return representation of a JSON string"""
    return json.loads(my_str)
