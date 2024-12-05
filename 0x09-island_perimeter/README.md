# 0x09 - Island Perimeter

This project is part of the 0x09 module at [Alx School](https://www.alxafrica.com/), where the goal is to solve algorithmic problems with a focus on working with grids and 2D arrays. The specific task is to calculate the perimeter of an island represented in a grid.

## Task Overview

### Problem Description

You are given a rectangular grid of `0`s and `1`s, where:
- `0` represents water,
- `1` represents land.

Each cell is a square with side length of `1`. The grid is completely surrounded by water, and there is only one island or no island at all.

### The goal:
Write a function `island_perimeter(grid)` that returns the perimeter of the island described in the grid.

### Input
- A 2D list `grid` of size `m x n` (where `1 <= m, n <= 100`).
- Each element in the grid is either `0` (water) or `1` (land).

### Output
- The function returns an integer representing the perimeter of the island formed by the land (`1`) cells.

### Constraints:
- The grid is rectangular with dimensions not exceeding 100x100.
- The grid is surrounded by water, and there is only one island or no island.
- The island does not contain any internal water pockets ("lakes").

## Function Prototype

```python
def island_perimeter(grid):
    pass
```

## Example

### Input:
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

### Outputs
```python
12
```


### Explanation

- The island consists of cells with value 1
- The perimeter of this island is 12, calculated by counting the exposed boundaries of the land cells, considering the surrounding water or the grid's boundary.

## Author

- [Martin Olutade](https://github.com/silgenius)