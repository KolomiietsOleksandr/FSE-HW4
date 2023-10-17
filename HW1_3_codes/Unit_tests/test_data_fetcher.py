import unittest
import responses
from data_fetcher import CustomDataFetcher

class TestCustomDataFetcher(unittest.TestCase):
    @responses.activate
    def test_get_custom_data_from_url(self):
        base_url = 'https://sef.podkolzin.consulting/api/users/lastSeen'
        responses.add(responses.GET, f"{base_url}?offset=0", json={"data": ["user1", "user2"]}, status=200)
        responses.add(responses.GET, f"{base_url}?offset=1", json={"data": ["user3", "user4"]}, status=200)
        responses.add(responses.GET, f"{base_url}?offset=2", json={"data": []}, status=200)

        data_fetcher = CustomDataFetcher()
        custom_data = data_fetcher.get_custom_data_from_url(base_url)

        expected_data = ["user1", "user2"]
        self.assertEqual(custom_data, expected_data)
