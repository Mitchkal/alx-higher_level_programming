#!/usr/bin/python3
"""
module 4-print_square
prints a square with #
"""


def print_square(size):
    """prints a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print("", end="")
    else:
        square = "\n".join("#" * size for i in range(size))
        print(square)
