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

    factor = 2
    operations = 0

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    # N is a prime number
    if n > 1:
        operations += n

    return operations
