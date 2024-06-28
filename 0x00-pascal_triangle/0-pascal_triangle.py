#!/usr/bin/python3
"""
Pascal's triangle module
"""


def pascal_triangle(n):
    """
    An implementation of pascal's triangle

    - Start with the first row
    - Implement each row by 1
    - Each new element is the sum of the two elements above it
    - Last element of each row is 1
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
