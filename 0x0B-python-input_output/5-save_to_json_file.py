#!/usr/bin/python3
"""module 5-save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """writes object to textfile using JSON"""
    import json

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
