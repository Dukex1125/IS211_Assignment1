#! usr/bin/env
# -*- coding: utf-8 -*-
"""Duke Phung Assignment 1 Part 1"""


def listDivide(number, divide=2):
    """Returns count of times items in number list is divisible by divide parameter without remainders.

    Args:
        number (list): list used to store items.
        divide (int, optional): value used as divider.

    Returns:
        int: count of how many items divisible by divider

    Example:
        >>>listDivider([1, 2, 3, 4 5])
        2
    """
    count = 0

    for x in number:
        try:
            y = int(x)
        except ValueError:
            pass
        else:
            if y % divide:
                pass
            else:
                count += 1

    return count
