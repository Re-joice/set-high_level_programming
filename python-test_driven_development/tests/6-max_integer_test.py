#!/usr/bin/python3
"""Unit tests for max_integer."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_beginning(self):
        """Test when the maximum is the first element."""
        self.assertEqual(max_integer([10, 4, 3, 2, 1]), 10)

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -2, -30]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 5, 3]), 5)

    def test_duplicate_maximum(self):
        self.assertEqual(max_integer([1, 5, 5, 2]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.2, 3.8, 2.5]), 3.8)

    def test_string(self):
        self.assertEqual(max_integer("Holberton"), "t")


if __name__ == "__main__":
    unittest.main()
