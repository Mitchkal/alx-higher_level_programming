#!/usr/bin/python3
"""
module 7-BaseGeometry
geometry class
methods:
    area(self)
"""


class BaseGeometry:
    """methods:
                area
                integer_validation
    """
    def area(self):
        """raises exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        args:
            name - a string
            value - an int
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
