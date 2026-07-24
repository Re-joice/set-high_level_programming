#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to modify.
        name (str): The attribute name.
        value: The attribute value.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
