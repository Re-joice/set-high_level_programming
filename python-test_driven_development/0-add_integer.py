#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """
    Add two integers.

    Floats are cast to integers before addition.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        The integer sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
