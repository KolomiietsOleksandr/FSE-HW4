import unittest
from user import CustomUser

class TestCustomUser(unittest.TestCase):
    def test_custom_user_initialization(self):
        user = CustomUser("John", "2023-09-27T10:00:00.000", True, None)
        self.assertEqual(user.username, "John")
        self.assertEqual(user.last_seen, "2023-09-27T10:00:00.000")
        self.assertTrue(user.is_online)

if __name__ == '__main__':
    unittest.main()

#python3 -m unittest test_user.py
