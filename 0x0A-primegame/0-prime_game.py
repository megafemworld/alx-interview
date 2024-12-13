#!/usr/env python3
"""
    Prime Game
"""

def isWinner(x, nums):
    """_summary_

    Args:
        x (_type_): _description_
        nums (_type_): _description_
    """
    if x == 0 or x == 1:
        return None
    if x % 2 == 0:
        return "Ben"
    return "Maria"