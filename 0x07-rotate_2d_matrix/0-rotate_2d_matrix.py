#!/usr/bin/python3
"""Rotate 2D Matrix in 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """1. Transponse th matrix
       2. Reverse each row
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
