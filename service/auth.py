from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET, JWT_ALGORITHM
import datetime
from service.user import UserService
from flask import abort
import calendar
import jwt


class AuthService:
    def __init__(self, user_service: UserService):
        self.service = user_service

    def generate_tokens(self, username, password):
        user = self.service.get_name(username)
        if not user:
            abort(400)
        if not self.service.compare_hash(user.password, password):
            abort(400)
        data = {
            'username': user.username,
            'role': user.role,
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
