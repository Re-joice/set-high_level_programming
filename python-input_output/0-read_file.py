#!/usr/bin/python3
"""Module for reading a UTF-8 text file and printing its contents."""


def read_file(filename=""):
    """Read a UTF-8 text file and print it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
