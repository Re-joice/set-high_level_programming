#!/usr/bin/python3
"""Module that prints a person's full name."""


def say_my_name(first_name, last_name=""):
    """Print the full name."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
