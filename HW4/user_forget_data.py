from flask import Flask, request, jsonify

class UserForgetDataHandler:
    def __init__(self, custom_users):
        self.custom_users = custom_users

    def forget_user_data(self, user_id):
        deleted_user = None
        for user in self.custom_users:
            if user.username == user_id:
                deleted_user = user
                self.custom_users.remove(user)
                break
        return deleted_user

    def create_flask_app(self):
        app = Flask(__name__)

        @app.route('/api/user/forget', methods=['POST'])
        def forget_user():
            user_id = request.args.get('userId')
            if user_id:
                deleted_user = self.forget_user_data(user_id)
                if deleted_user:
                    return jsonify({"userId": user_id})
                else:
                    return "User not found", 404
            return "User ID not provided", 400

        return app
