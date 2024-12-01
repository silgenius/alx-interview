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
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
