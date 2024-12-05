#!/usr/bin/python3

"""
Contains a function def island_perimeter(grid):
that returns the perimeter of the island
"""


def helper_cell(cell):
    if not cell:
        return 1
    return 0


def island_perimeter(grid) -> int:
    """a function called that calculates the perimeter
    of an island in a rectangular grid

    Args:
        grid (List of List(Int)): The rectangular grid

    Returns:
        int: the perimeter of an island calculated
    """

    perimeter = 0
    for row in range(1, len(grid) - 1):
        for cell in range(1, len(grid[row]) - 1):
            if grid[row][cell] == 1:
                perimeter += helper_cell(grid[row][cell - 1])
                perimeter += helper_cell(grid[row][cell + 1])
                perimeter += helper_cell(grid[row - 1][cell])
                perimeter += helper_cell(grid[row - 1][cell])
    return perimeter
