from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with
from flask_pymongo import PyMongo
from config import Development
from models import User

app = Flask(__name__)
app.config.from_object(Development)
api = Api(app)
mongo = PyMongo(app)

class UsersApiController(Resource):

    SCHEMA = {
        'name': fields.String,
        'email': fields.String,
        'role': fields.String
    }

    def get(self):
        return {'hello': 'world'}

    @marshal_with(SCHEMA)
    def post(self):
        user = User(mongo.db.users, **request.get_json())
        try:
            user.save()
            return user.toDICT(), 203
        except Exception as e:
            return {'name': str(e)}, 400


class UserApiController(Resource):

    def get(self, id=None):
        return {'hello': 'world'}

    def put(self, id=None):
        return {'hello': 'world'}

    def delete(self, id=None):
        return {'hello': 'world'}

api.add_resource(UsersApiController, '/users')
api.add_resource(UserApiController, '/users/<int:id>')

app.run()
