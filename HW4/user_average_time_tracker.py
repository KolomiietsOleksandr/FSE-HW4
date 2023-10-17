from datetime import datetime, timedelta
from flask import Flask, request, jsonify

class UserAverageTimeTracker:
    def __init__(self, custom_users):
        self.user_data = {}
        self.custom_users = custom_users

    def track_user_online_status(self):
        current_time = datetime.utcnow()
        for user in self.custom_users:
            if user.is_online:
                if user.username not in self.user_data:
                    self.user_data[user.username] = {"entry_time": current_time}
            else:
                if user.username in self.user_data:
                    self.user_data[user.username]["exit_time"] = current_time

    def calculate_daily_average(self, user_id):
        if user_id in self.user_data:
            entry_time = self.user_data[user_id]["entry_time"]
            exit_time = self.user_data[user_id]["exit_time"]
            total_time = (exit_time - entry_time).total_seconds()
            return total_time / 86400
        else:
            return 0

    def calculate_weekly_average(self, user_id):
        if user_id in self.user_data:
            entry_time = self.user_data[user_id]["entry_time"]
            exit_time = self.user_data[user_id]["exit_time"]
            total_time = (exit_time - entry_time).total_seconds()
            return total_time / 604800
        else:
            return 0

    def create_flask_app(self):
        app = Flask(__name__)

        @app.route('/api/stats/user/average', methods=['GET'])
        def get_average_times():
            user_id = request.args.get('userId')
            if user_id:
                daily_average = self.calculate_daily_average(user_id)
                weekly_average = self.calculate_weekly_average(user_id)
                return jsonify({"dailyAverage": daily_average, "weeklyAverage": weekly_average})
            return "User ID not provided", 400

        return app
