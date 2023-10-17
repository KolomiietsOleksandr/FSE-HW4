from user import CustomUser
from datetime import datetime

class CustomUserListGenerator:
    def get_custom_users(self, data):
        custom_user_list = []
        for user in data:
            username = user["nickname"]
            last_seen_date = user["lastSeenDate"]
            is_online = bool(user["isOnline"])
            #last_seen_time = user["lastSeenTime"]

            last_seen_time = None

            custom_user_data = CustomUser(username, last_seen_date, is_online, last_seen_time)
            custom_user_list.append(custom_user_data)
        return custom_user_list

    def custom_when_online(self, custom_users, current_time):
        for custom_user in custom_users:
            if custom_user.is_online:
                custom_user.last_seen = "online"
                custom_user.last_seen_time = current_time
            else:
                last = custom_user.last_seen[:23]
                last_seen_date = datetime.strptime(last, "%Y-%m-%dT%H:%M:%S.%f")
                difference = current_time - last_seen_date
                if difference.total_seconds() <= 30:
                    custom_user.last_seen = "just now"
                    custom_user.last_seen_time = last_seen_date
                elif 30 < difference.total_seconds() <= 60:
                    custom_user.last_seen = "less than a minute ago"
                    custom_user.last_seen_time = last_seen_date
                elif 1 < difference.total_seconds() / 60 <= 59:
                    custom_user.last_seen = "a couple of minutes ago"
                    custom_user.last_seen_time = last_seen_date
                elif 2 <= difference.total_seconds() / 3600 <= 119:
                    custom_user.last_seen = "an hour ago"
                    custom_user.last_seen_time = last_seen_date
                elif difference.total_seconds() / 3600 > 2 and last_seen_date.date() == current_time.date():
                    custom_user.last_seen = "today"
                    custom_user.last_seen_time = last_seen_date
                elif 1 < difference.total_days() <= 1:
                    custom_user.last_seen = "yesterday"
                    custom_user.last_seen_time = last_seen_date
                elif difference.total_days() < 7:
                    custom_user.last_seen = "this week"
                    custom_user.last_seen_time = last_seen_date
                else:
                    custom_user.last_seen = "a long time ago"
                    custom_user.last_seen_time = last_seen_date
