from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from decorators import auth_required, admin_required
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        data = genre_service.get_all()
        return GenreSchema(many=True).dump(data), 200

    @admin_required
    def post(self):
        data = genre_service.create(request.json)
        return GenreSchema(many=False).dump(data), 201


@genre_ns.route('/<id>')
class GenreView(Resource):
    @auth_required
    def get(self, id):
        data = genre_service.get_one(int(id))
        return GenreSchema().dump(data), 200

    @admin_required
    def delete(self, id):
        genre_service.delete(int(id))
        return "", 204

    @admin_required
    def update(self, id):
        genre_service.update(int(id), request.json)
        return "", 200
