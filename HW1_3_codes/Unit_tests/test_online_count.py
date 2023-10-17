import unittest
from datetime import datetime
from online_count import UserStatsController
from user import CustomUser

class TestUserStatsController(unittest.TestCase):

    def test_calculate_users_online_count(self):

        controller = UserStatsController()
        controller.users = [
            CustomUser("user1", "2023-10-08T10:00:00.000000", True, None),
            CustomUser("user2", "2023-10-08T11:00:00.000000", False, None),
            CustomUser("user3", "online", True, None),
            CustomUser("user4", "2023-10-08T09:00:00.000000", False, None),
        ]

        date1 = datetime(2023, 10, 8, 10, 30, 0)
        date2 = datetime(2023, 10, 8, 11, 30, 0)
        date3 = datetime(2023, 10, 8, 12, 0, 0)

        count1 = controller.calculate_users_online_count(date1)
        count2 = controller.calculate_users_online_count(date2)
        count3 = controller.calculate_users_online_count(date3)

        print(f"Count1: {count1}")
        print(f"Count2: {count2}")
        print(f"Count3: {count3}")

        self.assertEqual(count1, 2)
        self.assertEqual(count2, 2)
        self.assertEqual(count3, 2)

if __name__ == '__main__':
    unittest.main()
