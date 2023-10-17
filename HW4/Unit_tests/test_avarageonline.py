import unittest
from HW4.user_average_time_tracker import UserAverageTimeTracker
from HW1_3_codes.user import CustomUser
from datetime import datetime, timedelta

class TestUserAverageTimeTracker(unittest.TestCase):
    def test_calculate_daily_average(self):
        custom_users = [
            CustomUser("user1", "2023-10-01T10:00:00.000", True, None)
        ]
        tracker = UserAverageTimeTracker(custom_users)

        entry_time = datetime(2023, 10, 1, 10, 0, 0)
        exit_time = datetime(2023, 10, 1, 11, 30, 0)
        tracker.user_data["user1"] = {"entry_time": entry_time, "exit_time": exit_time}

        daily_average = tracker.calculate_daily_average("user1")
        self.assertEqual(daily_average, 0.0625)

    def test_calculate_weekly_average(self):
        custom_users = [
            CustomUser("user1", "2023-10-01T10:00:00.000", True, None)
        ]
        tracker = UserAverageTimeTracker(custom_users)

        entry_time = datetime(2023, 10, 1, 10, 0, 0)
        exit_time = datetime(2023, 10, 8, 11, 0, 0)
        tracker.user_data["user1"] = {"entry_time": entry_time, "exit_time": exit_time}

        weekly_average = tracker.calculate_weekly_average("user1")
        self.assertEqual(weekly_average, 1.005952380952381)

if __name__ == '__main__':
    unittest.main()
