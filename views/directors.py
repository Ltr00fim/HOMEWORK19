from flask_restx import Resource, Namespace
from flask import request
from dao.model.director import DirectorSchema
from decorators import auth_reguired, admin_reguired
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_reguired
    def get(self):
        data = director_service.get_all()
        return DirectorSchema(many=True).dump(data), 200

    @admin_reguired
    def post(self):
        data = director_service.create(request.json)
        return DirectorSchema(many=False).dump(data), 201


@director_ns.route('/<id>')
class DirectorView(Resource):
    @auth_reguired
    def get(self, id):
        data = director_service.get_one(int(id))
        return DirectorSchema().dump(data), 200

    @admin_reguired
    def delete(self, id):
        director_service.delete(int(id))
        return "", 204

    @admin_reguired
    def update(self, id):
        director_service.update(int(id), request.json)
        return "", 200