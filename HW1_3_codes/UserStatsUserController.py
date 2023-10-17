from datetime import datetime
from user_list_generator import CustomUserListGenerator

class UserStatsHistoryController:
    def __init__(self, custom_data):
        self.custom_user_list_generator = CustomUserListGenerator()
        self.custom_data = custom_data

    def get_user_history(self, user_id, requested_date):
        custom_users = self.custom_user_list_generator.get_custom_users(self.custom_data)
        user = next((user for user in custom_users if user.username == user_id), None)

        if user is None:
            return {"wasUserOnline": None, "nearestOnlineTime": None}, 404

        requested_datetime = datetime.strptime(requested_date, '%Y-%d-%m-%H:%M')
        was_user_online = user.is_online

        if not was_user_online:
            nearest_online_time = self.find_nearest_online_time(custom_users, requested_datetime)
        else:
            nearest_online_time = None

        return {
            "wasUserOnline": was_user_online,
            "nearestOnlineTime": nearest_online_time.strftime('%Y-%d-%m-%H:%M') if nearest_online_time else None
        }, 200

    def find_nearest_online_time(self, custom_users, requested_datetime):
        online_times = []
        current_time = datetime.utcnow()

        for custom_user in custom_users:
            if custom_user.is_online:
                online_times.append(current_time)
            else:
                last_seen = custom_user.last_seen[:23]
                last_seen_date = datetime.strptime(last_seen, "%Y-%m-%dT%H:%M:%S.%f")
                difference = current_time - last_seen_date

                if difference.total_seconds() <= 30:
                    online_times.append(last_seen_date)

        if online_times:
            return min(online_times, key=lambda x: abs(x - requested_datetime))
        else:
            return None
