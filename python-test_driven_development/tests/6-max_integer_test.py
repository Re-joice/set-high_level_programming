#!/usr/bin/python3
"""Unit tests for the max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_list(self):
        """Test an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list."""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-10, -2, -30]), -2)

    def test_mixed_numbers(self):
        """Test a list with positive and negative numbers."""
        self.assertEqual(max_integer([-1, 0, 5, 3]), 5)

    def test_duplicate_maximum(self):
        """Test duplicate maximum values."""
        self.assertEqual(max_integer([1, 5, 5, 2]), 5)

    def test_float_numbers(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.2, 3.8, 2.5]), 3.8)

    def test_string(self):
        """Test a string."""
        self.assertEqual(max_integer("Holberton"), "t")


if __name__ == "__main__":
    unittest.main()
