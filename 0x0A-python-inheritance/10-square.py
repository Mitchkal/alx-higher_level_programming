#!/usr/bin/python3
"""module 10-square
methods:
    Area(self)
    init(self, size)
with square subclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """grandchild of basegeometry"""
    def __init__(self, size):
        """initialise and validate"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
