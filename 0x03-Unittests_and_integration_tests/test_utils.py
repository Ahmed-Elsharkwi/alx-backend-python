#!/usr/bin/env python3
""" module for testing access_nested_map """
from flask import jsonify
import unittest
from typing import Dict, Tuple, Union, Callable
from unittest.mock import patch, Mock
from parameterized import parameterized


from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """class for testing"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple[str], expected: Union[Dict, int]
    ) -> None:
        """test access nested map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map: Dict, path: Tuple[str]
    ) -> None:
        """test accessnestedmap method and raise keyError incase of error"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class for testing get json function"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(
        self,
        url: str,
        payload: Dict,
    ) -> None:
        """test the get json function"""
        with patch("utils.requests.get") as mock_get:
            mokc_response = Mock()
            mokc_response.json.return_value = payload
            mock_get.return_value = mokc_response
            result = get_json(url)

        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """class for testing memoziation"""

    def test_memoize(self) -> None:
        """test memoization"""

        class TestClass:
            """Test class"""

            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_get:
            mock_get.return_value = 42
            obj = TestClass()
            result_1 = obj.a_property
            result_2 = obj.a_property

            mock_get.assert_called_once_with()

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)
