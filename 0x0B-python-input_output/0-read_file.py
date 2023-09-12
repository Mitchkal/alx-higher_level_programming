#!/usr/bin/python3
"""module 0-read_file"""


def read_file(filename=""):
    """reads file contents and prints to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
