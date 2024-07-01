#!/usr/bin/env python3
""" module for testing access_nested_map """
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
    def test_access_nested_map(self, nested_map, path, expected):
        """ test access nested map method """
        assert_equal(access_nested_map(nested_map, path), expected)
