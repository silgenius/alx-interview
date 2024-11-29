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
    memo = {}

    def helper(amount):
        # Base cases
        if amount < 0:
            return float('inf')  # impossible to make change
        if amount == 0:
            return 0  # no coins needed to make 0
        
        # If we've already computed the result for this amount, return it
        if amount in memo:
            return memo[amount]
        
        # Initialize the result to a large number
        min_coins = float('inf')
        
        
        # Try each coin and calculate the minimum number of coins needed
        for coin in coins:
            result = helper(amount - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)
        
        # Store the result in memo table
        memo[amount] = min_coins
        return min_coins
    
    # Call the helper function and get the result for the total
    result = helper(total)
    
    # If the result is still infinity, return -1 as it's impossible to make change
    return result if result != float('inf') else -1

