#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed to meet a given amount.
"""


def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to make the given total.

    Parameters:
    coins (list of int): The values of the available coins.
    total (int): The target amount.

    Returns:
    int: The minimum number of coins needed to meet total.
         If total is 0 or less, returns 0.
         If total cannot be met, returns -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    remaining = total

    for coin in coins:
        if remaining == 0:
            break
        count = remaining // coin
        num_coins += count
        remaining -= count * coin

    return num_coins if remaining == 0 else -1
