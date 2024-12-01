#!/usr/bin/python3

"""Contains makeChange function that determines
    the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, this algorithm determines
    the fewest number of coins needed to meet a given amount total

    Args:
        coins (int): coins given
        total (int): Total to be meet

    Returns:
        int: the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    check = 0
    operation = 0
    coins.sort(reverse=True)

    for coin in coins:
        while check < total:
            check += coin
            operation += 1
        if check == total:
            return operation
        check -= coin
        operation -= 1
    return -1
