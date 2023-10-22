import unittest
from HW1_3_codes.user import CustomUser
from HW1_3_codes.user_list_generator import CustomUserListGenerator
from HW1_3_codes.translator import CustomTranslator
from datetime import datetime
from HW1_3_codes.online_count import UserStatsController
from HW1_3_codes.UserStatsUserController import UserStatsHistoryController
from HW1_3_codes.user_online_predictor import UserOnlinePredictorWithPrediction
from HW1_3_codes.users_online_predictor import UserOnlinePredictor
from HW4.user_average_time_tracker import UserAverageTimeTracker
from HW4.UserOnlineTimeCalculator import UserTotalTimeOnlineTracker
from HW4.user_forget_data import UserForgetDataHandler

class TestE2E(unittest.TestCase):
    def test_e2e_workflow(self):
        custom_users = [
            CustomUser("User1", "2023-10-08T10:00:00.000", True, None),
            CustomUser("User2", "2023-10-08T11:00:00.000", False, None),
            CustomUser("User3", "2023-10-08T12:00:00.000", True, None),
        ]

        translator = CustomTranslator()
        for user in custom_users:
            user.username = translator.translate(user.username, "uk")

        controller = UserStatsController()
        controller.users = custom_users
        date1 = datetime(2023, 10, 8, 10, 30, 0)
        count1 = controller.calculate_users_online_count(date1)

        user_stats_history_controller = UserStatsHistoryController(custom_users)

        result, status_code = user_stats_history_controller.get_user_history("User1", "2023-10-08-10:30")
        nearest_online_time = user_stats_history_controller.find_nearest_online_time(custom_users, datetime.strptime("2023-10-08-10:30", '%Y-%d-%m-%H:%M'))

        user_online_predictor = UserOnlinePredictorWithPrediction(custom_users)
        prediction_result = user_online_predictor.predict_user_online("User1", "2023-10-08-11:00", 0.5)

        user_online_predictor = UserOnlinePredictor(custom_users)
        matching_users = [user for user in custom_users if user.is_online]
        average_online = user_online_predictor.calculate_average_users_online(matching_users)

        user_average_time_tracker = UserAverageTimeTracker(custom_users)
        user_id = "User1"
        entry_time = datetime(2023, 10, 8, 10, 0, 0)
        exit_time = datetime(2023, 10, 8, 11, 30, 0)
        user_average_time_tracker.user_data[user_id] = {"entry_time": entry_time, "exit_time": exit_time}
        daily_average = user_average_time_tracker.calculate_daily_average(user_id)

        user_average_time_tracker = UserAverageTimeTracker(custom_users)
        user_id = "User1"
        entry_time = datetime(2023, 10, 8, 10, 0, 0)
        exit_time = datetime(2023, 10, 15, 11, 0, 0)
        user_average_time_tracker.user_data[user_id] = {"entry_time": entry_time, "exit_time": exit_time}
        weekly_average = user_average_time_tracker.calculate_weekly_average(user_id)

        user_total_time_tracker = UserTotalTimeOnlineTracker(custom_users)
        user_id = "User1"
        entry_time = datetime(2023, 10, 8, 10, 0, 0)
        exit_time = datetime(2023, 10, 8, 11, 30, 0)
        user_total_time_tracker.user_data[user_id] = {"entry_time": entry_time, "exit_time": exit_time}
        total_time = user_total_time_tracker.get_total_time_online(user_id)

        user_forget_data_handler = UserForgetDataHandler(custom_users)
        user_to_forget = "User1"
        deleted_user = user_forget_data_handler.forget_user_data(user_to_forget)


if __name__ == '__main__':
    unittest.main()
