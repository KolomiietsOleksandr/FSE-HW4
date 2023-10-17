from datetime import datetime
from flask import Flask, request, jsonify

class UserTotalTimeOnlineTracker:
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

    def get_total_time_online(self, user_id):
        if user_id in self.user_data:
            entry_time = self.user_data[user_id]["entry_time"]
            exit_time = self.user_data[user_id]["exit_time"] if "exit_time" in self.user_data[user_id] else datetime.utcnow()
            total_time = (exit_time - entry_time).total_seconds()
            return {"totalTime": int(total_time)}
        else:
            return {"totalTime": 0}

    def create_flask_app(self):
        app = Flask(__name__)

        @app.route('/api/stats/user/total', methods=['GET'])
        def get_total_time_online():
            user_id = request.args.get('userId')
            if user_id:
                total_time = self.get_total_time_online(user_id)
                return jsonify(total_time)
            return "User ID not provided", 400

        return app
