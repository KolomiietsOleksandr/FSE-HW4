import unittest
from HW4.UserOnlineTimeCalculator import UserTotalTimeOnlineTracker
from HW1_3_codes.user import CustomUser
from datetime import datetime, timedelta

class TestUserTotalTimeOnlineTracker(unittest.TestCase):
    def test_get_total_time_online(self):
        custom_users = [
            CustomUser("user1", "2023-10-01T10:00:00.000", True, None),
            CustomUser("user2", "2023-10-01T11:00:00.000", True, None)
        ]
        tracker = UserTotalTimeOnlineTracker(custom_users)

        entry_time = datetime(2023, 10, 1, 10, 0, 0)
        exit_time = datetime(2023, 10, 1, 11, 30, 0)
        tracker.user_data["user1"] = {"entry_time": entry_time, "exit_time": exit_time}

        total_time = tracker.get_total_time_online("user1")
        self.assertEqual(total_time, {"totalTime": 5400})  # 1 hour and 30 minutes

        total_time = tracker.get_total_time_online("user3")
        self.assertEqual(total_time, {"totalTime": 0})

if __name__ == '__main__':
    unittest.main()
