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

    tri.append([1])
    if n == 1:
        return tri

    tri.append([1, 1])
    if n == 2:
        return tri

    for i in range(3, n + 1):
        x = [float('inf')] * i
        x[0] = 1
        x[-1] = 1
        for j in range(len(tri[i - 2]) - 1):
            x[j + 1] = tri[i - 2][j] + tri[i - 2][j + 1]
        tri.append(x)
        x = []
    return tri
