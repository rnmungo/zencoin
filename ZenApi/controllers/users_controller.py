from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Account, Currency, DEFAULT_CURRENCY_NAME
from tools import mongo_to_dict, ZenMail


class UsersApiController(Resource):

    def __init__(self, mail):
        self.mail = mail

    def post(self, **kwargs):
        content = request.get_json()
        try:
            # Registro de usuarios
            # TO DO: Rollback si falla algún guardado de datos.
            user = User(
                email=content.get('email', ''),
                first_name=content.get('first_name', ''),
                last_name=content.get('last_name', ''),
                role=content.get('role', ''),
                password=generate_password_hash(content.get('password', ''))
            ).save()
            # Creación de cuenta asociada al usuario
            # TO DO: Setear moneda por defecto en opciones.
            currency = Currency.objects(name=DEFAULT_CURRENCY_NAME).first()
            account = Account(
                user=mongo_to_dict(user, exclude_fields=['created_at', 'updated_at', 'password', 'role']),
                currency=mongo_to_dict(currency, exclude_fields=['created_at', 'updated_at']),
                saldo=0.,
                number=Account.objects.count()+1
            ).save()
            # Envío de e-mail de bienvenida.
            ZenMail.send_welcome_message(self.mail, user)
            return mongo_to_dict(account, exclude_fields=['created_at', 'updated_at']), 203
        except Exception:
            message = 'Error de servidor, vuelva a intentar más tarde. '
            message += 'Si el error persiste, contáctese con soporte.'
            return {'message': message}, 500


class UserApiController(Resource):

    def get(self, id=None):
        if id is None:
            return {'message': 'Error en la solicitud'}, 400
        user = User.objects(id=id).first()
        return mongo_to_dict(user), 200

    def put(self, id=None):
        # Cambio de contraseña
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
        # Autenticación de usuario
        content = request.get_json()
        user = User.objects(email=content.get('email', '')).first()
        if user is not None and \
            check_password_hash(user._data['password'], content.get('password', '')):
            return {'token': str(user.id)}, 200
        return {'message': "E-mail o contraseña incorrectos"}, 400
