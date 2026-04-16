import unittest
from unittest.mock import patch, MagicMock
import requests

from api_response_parser import parse_users, fetch_users_with_retry


class TestParseUsers(unittest.TestCase):

    def test_parse_users_basic(self):
        json_data = """
        {
          "payload": {
            "data": [
              {
                "id": 1,
                "profile": { "name": "Alice" },
                "contact": { "email": "alice@example.com" }
              }
            ]
          }
        }
        """

        users = parse_users(json_data)

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].id, 1)
        self.assertEqual(users[0].name, "Alice")
        self.assertEqual(users[0].email, "alice@example.com")

    def test_parse_users_null_contact(self):
        json_data = """
        {
          "payload": {
            "data": [
              {
                "id": 2,
                "profile": { "name": "Bob" },
                "contact": null
              }
            ]
          }
        }
        """

        users = parse_users(json_data)
        self.assertIsNone(users[0].email)

    def test_parse_users_empty_email(self):
        json_data = """
        {
          "payload": {
            "data": [
              {
                "id": 3,
                "profile": { "name": "Charlie" },
                "contact": { "email": "" }
              }
            ]
          }
        }
        """

        users = parse_users(json_data)
        self.assertIsNone(users[0].email)

    def test_parse_users_missing_profile(self):
        json_data = """
        {
          "payload": {
            "data": [
              {
                "id": 4,
                "profile": null
              }
            ]
          }
        }
        """

        users = parse_users(json_data)
        self.assertEqual(users[0].name, "Unknown")

    def test_parse_users_invalid_json(self):
        users = parse_users("INVALID JSON")
        self.assertEqual(users, [])


class TestFetchUsersWithRetry(unittest.TestCase):

    @patch("api_response_parser.requests.get")
    def test_fetch_users_with_retry_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
        {
          "payload": {
            "data": [
              { "id": 1, "profile": {"name": "Alice"}, "contact": {"email": "a@example.com"} }
            ]
          }
        }
        """
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        users = fetch_users_with_retry("http://dummy")

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, "Alice")

    @patch("api_response_parser.requests.get")
    def test_fetch_users_with_retry_timeout(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout

        users = fetch_users_with_retry("http://dummy", max_retries=2)

        self.assertEqual(users, [])

    @patch("api_response_parser.requests.get")
    def test_fetch_users_with_retry_http_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        users = fetch_users_with_retry("http://dummy")

        self.assertEqual(users, [])


if __name__ == "__main__":
    unittest.main()
