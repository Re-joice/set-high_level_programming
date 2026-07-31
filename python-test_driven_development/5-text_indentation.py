#!/usr/bin/python3
"""Module that prints text with indentation."""


def text_indentation(text):
    """
    Print text with two new lines after '.', '?' and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True

    for char in text:
        if new_line and char == " ":
            continue

        print(char, end="")

        if char in ".?:":
            print("\n")
            new_line = True
        else:
            new_line = False
