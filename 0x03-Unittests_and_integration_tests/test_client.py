#!/usr/bin/env python3
""" This module defines a test class
"""
import unittest
from unittest.mock import patch, Mock
from utils import get_json
from client import GithubOrgClient
import client
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ This class defines
        'test_org' function
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('utils.requests.get')
    def test_org(self, arg, mock_get):
        """ Tests the 'GithubOrgClient.org' method
        """
        obj = GithubOrgClient(arg)
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response
        data = obj.org
        self.assertEqual(data, {})
        mock_get.assert_called_with(f'https://api.github.com/orgs/{arg}')
        mock_get.assert_called_once()
