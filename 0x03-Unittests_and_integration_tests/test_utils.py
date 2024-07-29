#!/usr/bin/env python3
"""
unittests to parameteize a unit test
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap Class
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test case for test_access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """tests for access_nested_map exception
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestgetJson(unittest.TestCase):
    """test class for get_jjson"""
    @patch('requests.get')
    def test_get_json(self, mock_get):
        """test method for get_json"""
        test_case = [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False})
        ]
        for test_url, test_payload in test_case:

            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)
            mock_get.reset_mock()
