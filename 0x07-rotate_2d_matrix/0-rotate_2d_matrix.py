#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    
    Args:
    matrix (List[List[int]]): The 2D matrix to be rotated.
    
    Returns:
    None: The matrix is modified in-place.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    rotate90 = [[matrix[row][i] for row in range(rows - 1, -1, -1)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = rotate90[i][j]