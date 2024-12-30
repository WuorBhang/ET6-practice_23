#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test file for the `has_double_letter` function.

This test file verifies the correctness of the `has_double_letter` function,
which checks for the presence of consecutive duplicate letters in a string.

Run the tests using the command:
    python3 -m unittest test_double_letter.py

"""

import unittest

from solutions.double_letter import has_double_letter


class TestHasDoubleLetter(unittest.TestCase):
    """Unit tests for checking the present of a double letter through function."""

    def test_has_double_letter(self):
        """Test the `has_double_letter` function with multiple cases."""
        self.assertTrue(has_double_letter("hello"))  # Contains double letter
        self.assertTrue(has_double_letter("committee"))  # Contains multiple duplicates
        self.assertTrue(has_double_letter("bookkeeper"))  # Contains multiple duplicates

    def test_without_double_letters(self):
        """Test words that do not contain any consecutive duplicate letters."""
        self.assertFalse(has_double_letter("world"))
        self.assertFalse(has_double_letter("python"))
        self.assertFalse(has_double_letter("Wuor"))
        self.assertFalse(has_double_letter("Bhang"))

    def test_empty_and_single_character(self):
        """Test edge cases: empty string and single-character string inputs."""
        self.assertFalse(has_double_letter(""))
        self.assertFalse(has_double_letter("a"))

    def test_case_sensitivity(self):
        """Test case sensitivity of the `has_double_letter` function."""
        self.assertTrue(has_double_letter("AaAa"))  # Has double letter
        self.assertFalse(has_double_letter("Abcde"))  # No consecutive duplicates
