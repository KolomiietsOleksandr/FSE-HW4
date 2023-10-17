import unittest
from datetime import datetime
from user import CustomUser
from user_list_generator import CustomUserListGenerator
from data_fetcher import CustomDataFetcher
from translator import CustomTranslator

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://sef.podkolzin.consulting/api/users/lastSeen"
        self.language = "en"
        self.current_time = datetime.now()

    def test_custom_data_integration(self):
        data_fetcher = CustomDataFetcher()
        custom_data = data_fetcher.get_custom_data_from_url(self.base_url)

        list_generator = CustomUserListGenerator()
        custom_users = list_generator.get_custom_users(data=custom_data)

        translator = CustomTranslator()
        for custom_user in custom_users:
            custom_user.last_seen = translator.translate(custom_user.last_seen, self.language)

        list_generator.custom_when_online(custom_users, self.current_time)

        for custom_user in custom_users:
            self.assertIsInstance(custom_user, CustomUser)
            self.assertTrue(custom_user.username)
            self.assertTrue(custom_user.last_seen)
            self.assertTrue(custom_user.last_seen_time)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
