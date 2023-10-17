import unittest
from datetime import datetime
from user_online_predictor import UserOnlinePredictorWithPrediction
from user import CustomUser

class TestUserOnlinePredictorWithPrediction(unittest.TestCase):
    def setUp(self):
        self.custom_users = [
            CustomUser("user1", "offline", False, datetime(2023, 10, 1, 12, 0)),
            CustomUser("user1", "offline", False, datetime(2023, 9, 24, 8, 0)),
            CustomUser("user2", "offline", False, datetime(2023, 10, 1, 10, 0)),
            CustomUser("user2", "offline", False, datetime(2023, 9, 24, 9, 0)),
            CustomUser("user3", "offline", False, datetime(2023, 10, 1, 14, 0)),
        ]

    def test_predict_user_online_user_not_found(self):
        predictor = UserOnlinePredictorWithPrediction(self.custom_users)
        result = predictor.predict_user_online("non_existent_user", "2023-10-01-11:00", 0.5)
        self.assertFalse(result["willBeOnline"])
        self.assertAlmostEqual(result["onlineChance"], 0.0, delta=0.001)
        self.assertEqual(result["error"], "User not found.")

    def test_predict_user_online_invalid_date_format(self):
        predictor = UserOnlinePredictorWithPrediction(self.custom_users)
        result = predictor.predict_user_online("user1", "2023-10-01 11:00", 0.5)
        self.assertFalse(result["willBeOnline"])
        self.assertAlmostEqual(result["onlineChance"], 0.0, delta=0.001)
        self.assertEqual(result["error"], "Invalid date format.")

    def test_predict_user_online_no_history_data(self):
        predictor = UserOnlinePredictorWithPrediction(self.custom_users)
        result = predictor.predict_user_online("user3", "2023-10-01-11:00", 0.5)
        self.assertFalse(result["willBeOnline"])
        self.assertAlmostEqual(result["onlineChance"], 0.0, delta=0.001)
        self.assertEqual(result["error"], "No history data available for the user.")

if __name__ == '__main__':
    unittest.main()
