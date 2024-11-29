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

    for coin in coins:
        for t in range(coin, total + 1):
            if dp[t - coin] != float('inf'):
                dp[t] = min(dp[t], dp[t - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
