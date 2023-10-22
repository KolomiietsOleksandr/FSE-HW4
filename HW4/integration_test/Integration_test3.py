import unittest
from HW4.user_forget_data import UserForgetDataHandler
from HW4.user_average_time_tracker import UserAverageTimeTracker
from HW1_3_codes.user import CustomUser
from datetime import datetime

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.custom_users = [
            CustomUser("user1", "2023-10-18T08:00:00.000", True, None),
            CustomUser("user2", "2023-10-18T09:00:00.000", False, None),
        ]
        self.forget_handler = UserForgetDataHandler(self.custom_users)
        self.tracker = UserAverageTimeTracker(self.custom_users)

    def test_integration(self):
        user_id = "user1"
        deleted_user = self.forget_handler.forget_user_data(user_id)
        self.assertEqual(deleted_user.username, user_id)
        self.assertNotIn(deleted_user, self.custom_users)

        entry_time = datetime(2023, 10, 1, 10, 0, 0)
        exit_time = datetime(2023, 10, 1, 11, 30, 0)
        self.tracker.user_data["user1"] = {"entry_time": entry_time, "exit_time": exit_time}
        daily_average = self.tracker.calculate_daily_average("user1")
        self.assertEqual(daily_average, 0.0625)

        entry_time = datetime(2023, 10, 1, 10, 0, 0)
        exit_time = datetime(2023, 10, 8, 11, 0, 0)
        self.tracker.user_data["user1"] = {"entry_time": entry_time, "exit_time": exit_time}
        weekly_average = self.tracker.calculate_weekly_average("user1")
        self.assertEqual(weekly_average, 1.005952380952381)

if __name__ == '__main__':
    unittest.main()
