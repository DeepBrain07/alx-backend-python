#!/usr/bin/env python3
""" This module defines a test class
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ This class defines
        'test_access_nested_map' function
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
        ])
    def test_access_nested_map(self, arg1, arg2, res):
        """ Tests 'access_nested_map' function
        """
        data = access_nested_map(arg1, arg2)
        self.assertEqual(data, res)
