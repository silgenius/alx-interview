# 0x07. Rotate 2D Matrix

## Description

This repository contains a Python solution to the problem of rotating a 2D matrix 90 degrees clockwise. The task involves modifying the input matrix in-place to achieve the desired rotation without using extra space for a new matrix.

### Problem Description

Given a square matrix `n x n`, rotate the matrix 90 degrees clockwise in-place.

For example:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
```

After the function is called, the matrix should be rotated to:

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## Usage

To use the `rotate_2d_matrix function`, simply import the module and pass a 2D matrix to be rotated:

```python

from 0-rotate_2d_matrix import rotate_2d_matrix

matrix = [
    [1, 2],
    [3, 4]
]

rotate_2d_matrix(matrix)
print(matrix)

```

## Authors

- [Martin Olutade](https://github.com/silgenius/)