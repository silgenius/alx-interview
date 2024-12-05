#!/usr/bin/python3

"""
Contains a function def island_perimeter(grid):
that returns the perimeter of the island
"""


def island_perimeter(grid) -> int:
    """a function called that calculates the perimeter
    of an island in a rectangular grid

    Args:
        grid (List of List(Int)): The rectangular grid

    Returns:
        int: the perimeter of an island calculated
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:  # If the cell is land
                # Check the four possible directions (up, down, left, right)
                if i == 0 or grid[i - 1][j] == 0:  # Check top
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # Check bottom
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Check left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # Check right
                    perimeter += 1
    return perimeter
