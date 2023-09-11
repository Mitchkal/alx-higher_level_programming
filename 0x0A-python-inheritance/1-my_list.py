#!/usr/bin/python3

"""module1-my_list- inherits from list
"""


class MyList(list):
    """
    child class
    inherits from list
    methods:
        print_sorted(self)
    """
    def print_sorted(self):
        """prints sorted ascending order list"""
        print(sorted(self))
