#!/usr/bin/python3
"""
tackle the coin change problem.
"""


def makeChange(coins, total):
    """
    makeChange: determine the fewest number of coins
    needed to meet a given amount total
    args:
        coins- different denomination
        total- total number target
    """
    counter = 0
    # accumulated = 0
    if total <= 0:
        return counter

    coins.sort(reverse=True)
    for coin in coins:
        while total - coin >= 0:
            total -= coin
            counter += 1
        if total == 0:
            return counter
    return -1
