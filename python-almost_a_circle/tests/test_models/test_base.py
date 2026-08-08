#!/usr/bin/python3
"""Unit tests for the Base class."""

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def test_id_auto(self):
        """Test automatic ID assignment."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_id_assigned(self):
        """Test assigning a specific ID."""
        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """Test to_json_string with a dictionary."""
        result = Base.to_json_string([{"id": 12}])
        self.assertIsInstance(result, str)
        self.assertEqual(result, '[{"id": 12}]')

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        """Test from_json_string with JSON data."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)
        self.assertEqual(result, [{"id": 89}])


if __name__ == "__main__":
    unittest.main()
