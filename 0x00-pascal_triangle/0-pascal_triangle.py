#!/usr/bin/python3
"""
    Pascal's TrianglE
"""


def pascal_triangle(n):
    """pascal_triangle
     a list of lists of integers representing the Pascal’s triangle of n.
    Args:
        n (integer): a number always an integer
    """
    if n <= 0:
        return []
    pascal = [[1]]
    while len(pascal) != n:
        pascal.append([1] + [pascal[-1][i] + pascal[-1][i + 1]
                             for i in range(len(pascal[-1]) - 1)] + [1])
    return pascal
