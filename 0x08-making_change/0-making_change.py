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

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        dp[i] = min(dp[i], *[dp[i - coin] + 1 if i - coin >= 0 else float('inf') for coin in coins])

    return dp[total] if dp[total] != float('inf') else -1
