from flask import request
from flask_restful import Resource, abort
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from models import User, Account, Currency, DEFAULT_CURRENCY_NAME
from tools import mongo_to_dict, ZenMail
from .exceptions import (APIException,
                         MissingDataRequest,
                         ModelDoesNotExist)


class UsersApiController(Resource):

    def __init__(self, mail):
        self.mail = mail

    ##########################   Recursos   ##########################

    def post(self):
        # Registro de usuarios
        email, f_name, l_name, role, password = self.get_data(request.get_json())
        self.validate(email, f_name, l_name, role, password)
        try:
            user = User(email=email, first_name=f_name, last_name=l_name,
                    role=role, password=generate_password_hash(password)
                ).save()
            # Creación de cuenta asociada al usuario
            currency = self.get_default_currency()
            account = Account(
                user=mongo_to_dict(user,
                    exclude_fields=['created_at', 'updated_at', 'password', 'role']),
                currency=mongo_to_dict(currency,
                    exclude_fields=['created_at', 'updated_at']),
                saldo=0.,
                number=Account.objects.count()+1
            ).save()
            # Envío de e-mail de bienvenida.
            ZenMail.send_welcome_message(self.mail, user)
            return mongo_to_dict(account,
                exclude_fields=['created_at', 'updated_at']), 203
        except SMTPServerDisconnected:
            return {'message': 'Error al enviar el mail predeterminado.'}, 500
        except Exception as e:
            abort(e.code, str(e))

    ###########################   Métodos   ###########################

    def get_default_currency(self):
        currency = Currency.objects(name=DEFAULT_CURRENCY_NAME).first()
        if not currency:
            raise ModelDoesNotExist(Currency.__name__, DEFAULT_CURRENCY_NAME)
        return currency

    def validate(self, email, f_name, l_name, role, password):
        if not email:
            raise MissingDataRequest('email')
        if not f_name:
            raise MissingDataRequest('first_name')
        if not l_name:
            raise MissingDataRequest('last_name')
        if not password:
            raise MissingDataRequest('password')

    def get_data(self, content):
        email    = content.get('email', '')
        f_name   = content.get('first_name', '')
        l_name   = content.get('last_name', '')
        role     = content.get('role', 'customer')
        password = content.get('password', '')
        return email, f_name, l_name, role, password


class UserApiController(Resource):

    ##########################   Recursos   ##########################

    def get(self, id=None):
        self.id_is_valid(id)
        user = User.objects(id=id).first()
        if not user:
            raise ModelDoesNotExist(User.__name__, id)
        return mongo_to_dict(user, exclude_fields=['created_at', 'updated_at', 'password']), 200

    def put(self, id=None):
        # Cambio de contraseña
        self.id_is_valid(id)
        password, repeat = self.get_data(request.get_json())
        try:
            user = User.objects(id=id).first()
            user.password = generate_password_hash(password)
            user.save()
            return {'message': 'Contraseña modificada correctamente'}, 200
        except Exception as e:
            abort(e.code, str(e))

    ###########################   Métodos   ###########################

    def id_is_valid(self, id):
        if id is None:
            raise APIException(404, 'Recurso no encontrado')
        if len(id) != 24:
            raise ModelDoesNotExist(User.__name__, id)

    def validate(self, password, repeat):
        if not password:
            raise MissingDataRequest('password')
        if not repeat:
            raise MissingDataRequest('repeat_password')
        elif password != repeat:
            raise APIException(400, 'Las contraseñas deben coincidir')

    def get_data(self, content):
        password = content.get('password', '')
        repeat = content.get('repeat_password', '')
        self.validate(password, repeat)
        return password, repeat


class LoginApiController(Resource):

    ##########################   Recursos   ##########################

    def post(self):
        # Autenticación de usuario
        email, password = self.get_data(request.get_json())
        user = User.objects(email=email).first()
        if user and check_password_hash(user._data['password'], password):
            return {'token': str(user.id)}, 200
        raise APIException(400, 'E-mail y contraseña no coinciden')

    ###########################   Métodos   ###########################

    def validate(self, email, password):
        if not email:
            raise MissingDataRequest('email')
        if not password:
            raise MissingDataRequest('password')

    def get_data(self, content):
        email = content.get('email', '')
        password = content.get('password', '')
        self.validate(email, password)
        return email, password
