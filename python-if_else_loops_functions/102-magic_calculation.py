#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Performs the same operations as the given Python bytecode."""
    if a < b:
        return c
    if c > b:
        return a + b
    return (a * b) - c
