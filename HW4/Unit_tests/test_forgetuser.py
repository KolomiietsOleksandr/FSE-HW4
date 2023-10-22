import unittest
from HW4.user_forget_data import UserForgetDataHandler
from HW1_3_codes.user import CustomUser

class TestUserForgetDataHandler(unittest.TestCase):
    def setUp(self):
        self.custom_users = [
            CustomUser("user1", "2023-10-18T08:00:00.000", True, None),
            CustomUser("user2", "2023-10-18T09:00:00.000", False, None),
        ]
        self.handler = UserForgetDataHandler(self.custom_users)

    def test_forget_user_data_existing_user(self):
        user_id = "user1"
        deleted_user = self.handler.forget_user_data(user_id)
        self.assertEqual(deleted_user.username, user_id)
        self.assertNotIn(deleted_user, self.custom_users)

    def test_forget_user_data_non_existing_user(self):
        user_id = "nonexistent_user"
        deleted_user = self.handler.forget_user_data(user_id)
        self.assertIsNone(deleted_user)
        self.assertNotIn(user_id, [user.username for user in self.custom_users])

if __name__ == '__main__':
    unittest.main()
