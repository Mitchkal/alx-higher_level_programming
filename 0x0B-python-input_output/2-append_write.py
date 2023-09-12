#!/usr/bin/python3
"""module 2-append_write"""


def append_write(filename="", text=""):
    """writes string to text file"""
    with open(filename, 'a') as f:
        return (f.write(text))
