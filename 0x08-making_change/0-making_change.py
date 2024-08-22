#!/usr/bin/pyhton3
"""Determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """coins: list of the values of the coins in possession
           - If total is 0 or less, return 0
           - If total cannot be met by any number of coins you have, return -1
       Return fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    array = [float('inf')] * (total + 1)
    array[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            array[i] = min(array[i], array[i - coin] + 1)

    return array[total] if array[total] != float('inf') else -1
