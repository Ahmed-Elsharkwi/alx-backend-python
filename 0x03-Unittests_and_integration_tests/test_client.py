#!/usr/bin/env python3
""" module for testing client """
import unittest
from typing import Dict, Tuple, Union, Callable
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD

# Create parameter sets from the TEST_PAYLOAD tuples
parameter_sets = [
    {
        "org_payload": org,
        "repos_payload": repos,
        "expected_repos": expected,
        "apache2_repos": apache2
    }
    for org, repos, expected, apache2 in TEST_PAYLOAD
]


class TestGithubOrgClient(unittest.TestCase):
    """class for testing org function"""

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json")
    def test_org(self, url: str, mock_get: Callable) -> None:
        """test the org function"""
        response = {"payload": True}
        mock_get.return_value = response

        object_1 = GithubOrgClient(url)
        result = object_1.org

        self.assertEqual(result, response)

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    def test_public_repos_url(self, url: str) -> None:
        """test the puplic repos_url"""
        with patch(
                "client.GithubOrgClient.org", new_callable=PropertyMock) as m:
            result = {"repos_url": True}
            m.return_value = result

            obj = GithubOrgClient(url)
            self.assertEqual(obj._public_repos_url, True)

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    @patch("client.get_json")
    def test_public_repos(self, url: str, mock_get_json: Callable) -> None:
        """test public repos method"""
        mock_get_json.return_value = [{"name": "Fuck"}]

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos:
            mock_public_repos.return_value = "You"
            obj = GithubOrgClient(url)

            repos = obj.public_repos()
            self.assertListEqual(repos, ["Fuck"])
            mock_public_repos.assert_called_once()

        mock_get_json.assert_called_once_with("You")

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, dict_1: Dict, lic: str, res: bool) -> None:
        """ test the has_license function """
        obj = GithubOrgClient("url")

        self.assertEqual(obj.has_license(dict_1, lic), res)


@parameterized_class(parameter_sets)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test for GithubOrgClient.public_repos """

    @classmethod
    def setUpClass(cls):
        """Mock requests.get to return example payloads"""
        cls.get_patcher = patch("utils.requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            mock_response = Mock()
            if url == "https://api.github.com/orgs/google":
                mock_response.json.return_value = cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                mock_response.json.return_value = cls.repos_payload
            return mock_response

        cls.mock_get.side_effect = side_effect

    def test_public_repos(self):
        """Test public_repos method returns expected results"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()
