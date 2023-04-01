from flask_restx import Namespace, Resource

from decorators import admin_reguired, auth_reguired
from implemented import user_service
from flask import request

user_ns = Namespace("users")


@user_ns.route("/")
class UsersView(Resource):
    def get(self):
        return user_service.get_all(), 200

    def post(self):
        data = request.json
        user_service.create(data)
        return "", 201


@user_ns.route("/<data>")
class UserView(Resource):
    def get(self, name):
        return user_service.get_name(name), 200

    def update(self):
        data = request.json
        user_service.update(data)
        return "", 204

    def delete(self, pk):
        user_service.delete(int(pk))
        return "", 204
