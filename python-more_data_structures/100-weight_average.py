#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple."""
    if not my_list:
        return 0

    total = 0
    weight = 0

    for score, w in my_list:
        total += score * w
        weight += w

    return total / weight
