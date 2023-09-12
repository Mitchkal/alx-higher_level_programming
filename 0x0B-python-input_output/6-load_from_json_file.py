#!/usr/bin/python3
"""module 6-load_from_json_file"""


def load_from_json_file(filename):
    """loads textfile from JSON"""
    import json

    with open(filename, mode='r', encoding="utf-8") as f:
        return json.load(f)
