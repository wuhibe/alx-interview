#!/usr/bin/python3
""" module for task 0
"""


def rotate_2d_matrix(matrix):
    """ method to rotate a 2d matrix
        counterclockwise
    """
    n = len(matrix)
    m2 = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            m2[i][n - j - 1] = matrix[j][i]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = m2[i][j]
