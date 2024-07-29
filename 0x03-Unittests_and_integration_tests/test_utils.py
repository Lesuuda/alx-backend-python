#!/usr/bin/env python3
"""
unittests to parameteize a unit test
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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


class TestGetJson(unittest.TestCase):
    """test class for get_jjson"""
    @parameterized.expand([
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """test method for get_json"""
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """test class for memoize"""
    def test_memoize(self):
        """test method for memoize"""
        class TestClass:
            """test class inside test_memoize"""
            def a_method(self):
                """a method that returns 42 """
                return 42

            @memoize
            def a_property(self):
                """returns a method"""
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock.assert_called_once()
