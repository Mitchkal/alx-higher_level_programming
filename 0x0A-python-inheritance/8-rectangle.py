#!/usr/bin/python3
"""module 9-rectangle
inherits from Basegeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """full ectangle with validator"""
    def __init__(self, width, height):
        """initailizes and validates"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
