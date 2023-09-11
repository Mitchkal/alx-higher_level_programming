#!/usr/bin/python3
"""
module 8-BaseGeometry
geometry class
with inheritance rectangle class
methods:
    area(self)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """child class
    methods:
            __init__(self, width, height
            area(self)
            __str__
    """
    def __init__(self, width, height):
        """initialiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """returns area; extension of parent class"""
        return self.__width * self.__height

    def __str__(self):
        """returns rectangle description"""
        return ("[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                          self.__width, self.__height))
