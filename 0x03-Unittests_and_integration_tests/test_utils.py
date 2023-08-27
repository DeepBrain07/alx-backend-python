#!/usr/bin/env python3
""" This module defines a test class
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
import utils


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

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
        ])
    def test_access_nested_map_exception(self, arg1, arg2):
        """ Raises an exception when neccessary
        """
        with self.assertRaises(KeyError):
            access_nested_map(arg1, arg2)

class TestGetJson(unittest.TestCase):
    """ This class defines
        'get_json' function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, arg, res):
        """ Tests 'get_json' function
        """
        with unittest.mock.patch('utils.requests.get') as mock_get:
            mock_response = unittest.mock.MagicMock()
            mock_response.json.return_value = res
            mock_get.return_value = mock_response
            data = get_json(arg)
            mock_get.assert_called_once()
            self.assertEqual(data, res)
