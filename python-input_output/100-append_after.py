#!/usr/bin/python3
"""Module for inserting text after matching lines in a file."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line after each line containing a given string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
