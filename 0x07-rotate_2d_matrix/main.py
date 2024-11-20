#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3, 5],
              [4, 5, 6, 8],
              [7, 8, 9, 2],
              [2, 3, 4, 5]]

    rotate_2d_matrix(matrix)
    print(matrix)