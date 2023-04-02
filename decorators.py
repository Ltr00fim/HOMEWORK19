from flask import request, abort
from config import Config
import jwt


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        try:
            token = request.headers['Authorization'].split('Bearer ')[-1]
            data = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM])
            return func(*args, **kwargs)
        except Exception:
            abort(401)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        try:
            token = request.headers['Authorization'].split('Bearer ')[-1]
            data = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM])
            print(data)
            if data['role'] == 'admin':
                return func(*args, **kwargs)
            abort(403)
        except Exception:
            raise

    return wrapper
