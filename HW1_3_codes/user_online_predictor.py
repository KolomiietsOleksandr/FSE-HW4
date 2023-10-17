from datetime import datetime, timedelta

class UserOnlinePredictorWithPrediction:
    def __init__(self, custom_users):
        self.custom_users = custom_users

    def predict_user_online(self, user_id, requested_datetime_str, tolerance):
        try:
            requested_datetime = datetime.strptime(requested_datetime_str, '%Y-%m-%d-%H:%M')
        except ValueError:
            return {"willBeOnline": False, "onlineChance": 0.0, "error": "Invalid date format."}

        user = next((user for user in self.custom_users if user.username == user_id), None)

        if user is None:
            return {"willBeOnline": False, "onlineChance": 0.0, "error": "User not found."}

        history_start = requested_datetime - timedelta(days=7)

        matching_users = [
            u for u in self.custom_users if
            u.last_seen != "online" and
            u.username == user_id and
            history_start <= u.last_seen_time <= requested_datetime
        ]

        total_weeks = 7

        if not matching_users:
            return {"willBeOnline": False, "onlineChance": 0.0, "error": "No history data available for the user."}

        online_chance = len(matching_users) / total_weeks

        return {"willBeOnline": online_chance >= tolerance, "onlineChance": online_chance}
