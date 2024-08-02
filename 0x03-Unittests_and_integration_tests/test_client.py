#!/usr/bin/env python3
"""tests for tge client class"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from clients import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
    """class for testting client"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("clients.get_json")
    def test_org(self, org_name, mock):
        """test for org function"""
        mock.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        result = client.org
        mock.assert_called_once_with(client.ORG_URL.format(org=org_name))
        self.assertEqual(result, {"login": org_name})
