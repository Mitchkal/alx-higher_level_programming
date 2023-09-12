#!/usr/bin/python3
"""module 11-student"""


class Student:
    """
    defines a student class
    attributes:
        first_name
        last_name
        age
    methods:
        __init__(self, first_name, last_name)
        to_json(self)
    """

    def __init__(self, first_name, last_name, age):
        """initializes student classs"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves dictionary representations of
        list, dictionary, string for json
        serialization
        """
        serial_dict = {}
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    serial_dict[attr] = getattr(self, attr)
            return serial_dict

    def reload_from_json(self, json):
        """replaces all attributes from json dict"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
