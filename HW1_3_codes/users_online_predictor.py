from datetime import datetime, timedelta

class UserOnlinePredictor:
    def __init__(self, custom_users):
        self.custom_users = custom_users

    def predict_users_online(self, requested_datetime_str):
        try:
            requested_datetime = datetime.strptime(requested_datetime_str, '%Y-%d-%m-%H:%M')
        except ValueError:
            return "Invalid date format."

        history_start = requested_datetime - timedelta(days=7)

        matching_users = [
            user for user in self.custom_users if
            user.last_seen != "online" and
            history_start <= user.last_seen_time <= requested_datetime
        ]

        average_users_online = self.calculate_average_users_online(matching_users)

        return {
            "onlineUsers": average_users_online
        }

    def calculate_average_users_online(self, matching_users):
        if matching_users:
            average_users_online = len(matching_users) / 7
        else:
            average_users_online = 0

        return average_users_online
