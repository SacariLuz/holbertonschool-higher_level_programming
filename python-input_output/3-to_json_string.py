#!/usr/bin/python3
"""Defines a string to json function"""


def to_json_string(my_obj):
    import json
    """return the json"""
    return json.dumps(my_obj)
