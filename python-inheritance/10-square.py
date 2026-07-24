#!/usr/bin/python3
"""Defines the Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a Square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
