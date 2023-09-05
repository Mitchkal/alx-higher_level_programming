#!/usr/bin/python3
"""
Module 1-rectangle
defines rectangle class wih private
instance attribute width
"""


class Rectangle:

    """
    square class definition

    Args:
        size : square side length
    """
    def __init__(self, width=0, height=0):
        """
        rectangle initialization

        Attributes:
            size : the rectangel side
            width: the width
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width
        args:
            value: an int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        args:
            value: the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
