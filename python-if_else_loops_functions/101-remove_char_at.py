#!/usr/bin/python3
def remove_char_at(str, n):
    """Returns a copy of the string with the character at index n removed."""
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n + 1:]
