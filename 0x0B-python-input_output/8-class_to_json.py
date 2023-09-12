#!/usr/bin/python3
"""module 8-class_to_json"""


def class_to_json(obj):
    """returns dictionary description"""
    serial_object = {}
    for attr_name, attr_value in obj.__dict__.items():

        if isinstance(attr_value, (list, dict, str, int, bool)):
            serial_object[attr_name] = attr_value

    return serial_object
