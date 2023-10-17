import unittest
from users_online_predictor import UserOnlinePredictor
from user import CustomUser

class TestUserOnlinePredictor(unittest.TestCase):
    def setUp(self):

        self.custom_users = [
            CustomUser("User1", "today", True, None),
            CustomUser("User2", "yesterday", False, None),
            CustomUser("User3", "2023-10-05T15:30:00.000", False, None),
        ]
        self.predictor = UserOnlinePredictor(self.custom_users)


    def test_calculate_average_users_online(self):
        matching_users = [
            CustomUser("User4", "2023-10-10T12:00:00.000", False, None),
            CustomUser("User5", "2023-10-10T13:00:00.000", False, None),
            CustomUser("User6", "2023-10-10T14:00:00.000", False, None),
        ]
        average = self.predictor.calculate_average_users_online(matching_users)
        self.assertAlmostEqual(average, 0.42857142857142855, places=6)


if __name__ == '__main__':
    unittest.main()
