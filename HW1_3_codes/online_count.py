from datetime import datetime
import requests
import json

class UserStatsController:
    baseurl = "https://sef.podkolzin.consulting/api/users/lastSeen"
    desiredCount = 217

    def __init__(self):
        self.dataFetcher = DataFetcher()
        self.data = self.dataFetcher.get_from_url(self.baseurl, self.desiredCount)

        self.userListGenerator = UserListGenerator()
        self.users = self.userListGenerator.get_users(self.data)

    class UserStatsResponse:
        def __init__(self, users_online):
            self.UsersOnline = users_online

    def get_users_online_stats(self, date):
        try:
            requested_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return "Invalid date format."

        users_online = self.calculate_users_online_count(requested_date)

        response = self.UserStatsResponse(users_online)

        return response

    def calculate_users_online_count(self, date):
        return sum(1 for user in self.users if self.is_user_online_at_date(user, date))

    def is_user_online_at_date(self, user, date):
        return user.is_online or user.last_seen.lower() == "online"


class CustomUser:
    def __init__(self, username, last_seen, is_online):
        self.username = username
        self.last_seen = last_seen
        self.is_online = is_online


class DataFetcher:
    def get_from_url(self, base_url, desired_count):
        custom_all_data = []
        max_offset = 10  # You can adjust this value as needed

        for offset in range(max_offset):
            if len(custom_all_data) >= desired_count:
                break

            url = f"{base_url}?offset={offset}"
            response = requests.get(url)

            if response.status_code == 200:
                json_content = response.text

                try:
                    container = json.loads(json_content)
                    custom_user_data = container["data"]
                    remaining_custom_users = desired_count - len(custom_all_data)
                    custom_users_to_add = min(len(custom_user_data), remaining_custom_users)
                    custom_all_data.extend(custom_user_data[:custom_users_to_add])
                except json.JSONDecodeError as ex:
                    print(f"Failed to parse JSON: {ex}")
            else:
                print(f"Failed to fetch data for offset {offset}")

        return custom_all_data


class UserListGenerator:
    def get_users(self, data):
        custom_user_list = []

        for user in data:
            username = user["nickname"]
            last_seen_date = user["lastSeenDate"]
            is_online = bool(user["isOnline"])
            custom_user_data = CustomUser(username, last_seen_date, is_online)
            custom_user_list.append(custom_user_data)

        return custom_user_list

if __name__ == "__main__":
    controller = UserStatsController()
    date = "2023-10-01"  # Замените эту строку на желаемую дату
    result = controller.get_users_online_stats(date)
    print(f"Users Online: {result.UsersOnline}")



