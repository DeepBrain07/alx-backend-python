#!/usr/bin/env python3
""" This module defines a test class
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
import utils
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

    @patch('utils.requests.get')
    def test_public_repos_url(self, mock_get):
        """ Tests the '_public_repos_url' property
        """
        obj = GithubOrgClient('abc')
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)\
                as mock_method:
            mock_method.return_value = \
                {'org_name': 'abc', 'repos_url': 'http://repost.url.com'}
            repos_url = obj._public_repos_url
            self.assertEqual(repos_url, mock_method.return_value['repos_url'])
            mock_response = Mock()
            mock_response.json.return_value = \
                [
                    {'name': 'payload1', 'license': {'key': 'key1234'}},
                    {'name': 'payload2', 'license': {'key': 'key9876'}}
                ]
            mock_get.return_value = mock_response
            self.assertEqual(obj.public_repos('key1234'), ['payload1'])
