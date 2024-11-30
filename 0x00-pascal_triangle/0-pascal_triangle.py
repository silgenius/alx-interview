#!/usr/bin/python3

"""
Contain a function def pascal_triangle(n): that returns a list of
lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Generate the first n rows of Pascal's triangle

    Args:
        n (int): amount or rows to generate

    Returns:
        List[List(int)]: _description_
    """
    if n <= 0:
        return []
    tri = []
    
    for i in range(n):
        x = [1] * (i + 1)
        for j in range(1, i):
            x[j] = tri[i - 1][j - 1] + tri[i - 1][j]
        tri.append(x)
    return tri
