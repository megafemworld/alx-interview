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
    B = 0
    M = 0
    count = 0
    if x < 1 or nums is None:
        return None
    for n in nums:
        if count > x:
            break
        if n == 2:
            B += 1
            continue
        prime = 0
        for r in range(2, n+1):
            if r == 2:
                prime += 1
                continue
            elif r % 2 != 0:
                prime += 1
        if prime % 2 == 0:
            M += 1
        else:
            B += 1
        count += 1
    if B > M:
        return 'Maria'
    if M > B:
        return 'Ben'
    else:
        return None
