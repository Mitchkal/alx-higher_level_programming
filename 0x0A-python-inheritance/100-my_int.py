#!/usr/bin/python3
"""module 100-my_int
inherits from int
handles rebels
"""


class MyInt(int):
    """overwides eq and inverts behavior"""
    def __eq__(self, other):
        """overrides eq"""
        return super().__ne__(other)

    def __ne__(self, other):
        """overwrides ne"""
        return super().__eq__(other)
