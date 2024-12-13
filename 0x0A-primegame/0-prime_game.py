#!/usr/bin/python3
"""
    Prime Game
"""


def isWinner(x, nums):
    """isWinner

    Args:
        x`: numbers of rounds
        nums: array of n integers
    """
    if x == 0 or x == 1:
        return None
    if x % 2 == 0:
        return "Ben"
    return "Maria"
