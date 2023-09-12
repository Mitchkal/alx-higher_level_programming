#!/bin/usr/python3
"""module 9-student"""


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

    def to_json(self):
        """retrieves dictionary representations of class"""
        serial_dict = {}
        for name, attribute in self.__dict__.items():
            serial_dict[name] = attribute
        return serial_dict
