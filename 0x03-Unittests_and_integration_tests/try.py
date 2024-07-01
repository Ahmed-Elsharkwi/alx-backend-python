#!/usr/bin/env python3
""" module for testing access_nested_map """
from typing import Dict, Tuple, Union
from utils import access_nested_map
from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ class for testing """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, str]) -> None:
        """ test access nested map method """
        self.assertEqual(access_nested_map(nested_map, path), expected)
