#!/usr/bin/env python3
""" module for testing access_nested_map """
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized


from utils import (

    access_nested_map,

    get_json,

    memoize,

)


class TestAccessNestedMap(unittest.TestCase):
    """ class for testing """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]) -> None:
        """ test access nested map method """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self,
            nested_map: Dict,
            path: Tuple[str]) -> None:
        """ test accessnestedmap method and raise keyError incase of error """
        with self.assertRaise(KeyError):
            access_nested_map(nested_map, path)
