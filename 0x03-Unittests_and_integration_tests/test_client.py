#!/usr/bin/env python3
""" module for testing client """
import unittest
from typing import Dict, Tuple, Union, Callable
from unittest.mock import patch, Mock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ class for testing org function """
    @parameterized.expand([
         ("google"),
         ("abc"),
         ])
    @patch("client.get_json")
    def test_org(
            self,
            url: str,
            mock_get: Callable) -> None:
        """test the org function """
        response = {"payload": True}
        mock_get.return_value = response

        object_1 = GithubOrgClient(url)
        result = object_1.org

        self.assertEqual(result, response)
