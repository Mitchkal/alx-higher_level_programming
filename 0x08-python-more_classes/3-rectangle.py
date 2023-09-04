#!/usr/bin/python3
"""
Module 3-rectangle
defines rectangle class wih private
instance attribute width and height

Methods:
    area(self) gets area
    perimet(self) gets perimeter

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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ finds and returns rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """finds and returns rectanle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """prints string equivalent of rectangle with #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rect = "\n".join(["#" * self.__width for rows in
                              range(self.__height)])
            return rect
