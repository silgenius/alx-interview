#!/usr/bin/python3

"""
contains a function minOperations that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """a method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): Number of H's

    Returns:
        int: Number of operations
    """
    if n <= 1:
        return 0

    num_of_H = 1
    num_of_operation = 0
    factors = []

    for i in range(2, int((n ** 0.5)) + 1):
        if n % i == 0:
            factors.append(i)

    if factors:
        a = factors[-1]  # i is a factor of n
    else:
        a = n

    b = n // a
    copy = num_of_H
    num_of_operation += 1

    if num_of_H != a:
        # Pasting
        num_of_H *= a
        num_of_operation += (num_of_H - 1)

        if n != num_of_H:
            copy = num_of_H
            num_of_operation += 1
            # Paste what is in copy
            num_of_H += copy * (b - 1)
            num_of_operation += (b - 1)
    return num_of_operation
