#!/usr/bin/python3
"""module 1-write_file"""


def write_file(filename="", text=""):
    """writes string to text file"""
    with open(filename, 'w') as f:
        return (f.write(text))
