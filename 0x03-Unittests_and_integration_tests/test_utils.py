#!/usr/bin/env python3
""" This module defines a test class
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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
        'test_get_json' function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, arg, res):
        """ Tests 'get_json' function
        """
        with unittest.mock.patch('utils.requests.get') as mock_get:
            mock_response = unittest.mock.Mock()
            mock_response.json.return_value = res
            mock_get.return_value = mock_response
            data = get_json(arg)
            mock_get.assert_called_once()
            self.assertEqual(data, res)


class TestMemoize(unittest.TestCase):
    """ This class defines
        'test_memoize' function
    """
    def test_memoize(self):
        """ Tests 'memoize' function
        """
        class TestClass:
            """ A test class
            """
            def a_method(self):
                """ Returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """ Returns 'a_method' defined above
                """
                return self.a_method()

        obj = TestClass()
        with unittest.mock.patch.object(obj, 'a_method') as mocked_method:
            mocked_method.return_value = 42
            d = obj.a_property
            c = obj.a_property
            self.assertEqual(d, 42)
            self.assertEqual(c, 42)
            mocked_method.assert_called_once()
