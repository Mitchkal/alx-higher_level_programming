#!/usr/bin/python3
"""module 12-pascal_triangle"""


def pascal_triangle(n):
    """returns a pascal's triangle"""
    if n <= 0:
        return []
    else:
        triangle = []
        for row in range(n):
            current_row = []
            for col in range(row + 1):
                if col == 0 or col == row:
                    current_row.append(1)
                else:
                    value = triangle[row - 1][col - 1] + triangle[row - 1][col]
                    current_row.append(value)
            triangle.append(current_row)
        return triangle
