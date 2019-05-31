from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from models import mongo_to_dict


class UsersApiController(Resource):

    def get(self):
        users = User.objects.all()
        return dict([(str(i), mongo_to_dict(user)) for i, user in enumerate(users, start=1)])

    def post(self):
        content = request.get_json()
        try:
            user = User(
                email=content.get('email', ''),
                first_name=content.get('first_name', ''),
                last_name=content.get('last_name', ''),
                role=content.get('role', ''),
                password=generate_password_hash(content.get('password', ''))
            ).save()
            return mongo_to_dict(user, exclude_fields=['created_at', 'updated_at', 'password']), 203
        except Exception as e:
            return {'message': str(e)}, 400


class UserApiController(Resource):

    def get(self, id=None):
        if id is None:
            return {'message': 'Error en la solicitud'}, 400
        user = User.objects(id=id).first()
        return mongo_to_dict(user), 200

    def put(self, id=None):
        if id is None:
            return {'message': 'Error en la solicitud'}, 400
        content = request.get_json()
        password = content.get('password', '')
        repeat_password = content.get('repeat_password', '')
        if not password or not repeat_password:
            return {'message': 'Error en la solicitud'}, 400
        elif password != repeat_password:
            return {'message': 'Las contraseñas deben de coincidir'}, 400
        try:
            user = User.objects(id=id).first()
            user.password = generate_password_hash(password)
            user.save()
        except Exception as e:
            return {'message': 'Error al guardar contraseñas'}, 400
        return {'message': 'Contraseña modificada correctamente'}, 200


class LoginApiController(Resource):

    def post(self):
        content = request.get_json()
        user = User.objects(email=content.get('email', '')).first()
        if user is not None and \
            check_password_hash(user._data['password'], content.get('password', '')):
            return {'token': str(user.id)}, 200
        return {'message': "E-mail o contraseña incorrectos"}, 400
