from flask_restx import Namespace, Resource
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


@user_ns.route("/<id>")
class UserView(Resource):
    def get(self, id):
        return user_service.get_name(id), 200

    def update(self):
        data = request.json
        user_service.update(data)
        return "", 204

    def delete(self, id):
        user_service.delete(int(id))
        return "", 204
