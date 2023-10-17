import unittest
from user_list_generator import CustomUserListGenerator

class TestCustomUserListGenerator(unittest.TestCase):
    def setUp(self):
        self.user_list_generator = CustomUserListGenerator()

    def test_get_custom_users(self):
        data = [{"nickname": "John", "lastSeenDate": "2023-09-27T10:00:00.000", "isOnline": True, "lastSeenTime": None}]
        custom_users = self.user_list_generator.get_custom_users(data)
        self.assertEqual(len(custom_users), 1)
        self.assertEqual(custom_users[0].username, "John")

if __name__ == '__main__':
    unittest.main()

#python3 -m unittest test_user_list_generator.py
