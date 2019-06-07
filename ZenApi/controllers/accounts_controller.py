from flask import request
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash, check_password_hash
from models import Account, User, Currency
from tools import mongo_to_dict
from db import Q
from .exceptions import (APIException,
                         MissingDataRequest,
                         ModelDoesNotExist)


class AccountsApiController(Resource):

    ##########################   Recursos   ##########################

    def post(self):
        # Creación de cuenta.
        user_id, currency_id, saldo = self.get_data(request.get_json())
        user, currency, saldo = self.get_models(user_id, currency_id, saldo)
        try:
            account = Account(
                user=mongo_to_dict(user, exclude_fields=['created_at', 'updated_at', 'password']),
                currency=mongo_to_dict(currency, exclude_fields=['created_at', 'updated_at']),
                saldo=saldo,
                number=Account.objects.count()+1
            ).save()
            return mongo_to_dict(account, exclude_fields=['created_at', 'updated_at']), 200
        except Exception as e:
            abort(e.code, str(e))

    ###########################   Métodos   ###########################

    def get_models(self, user_id, currency_id, saldo):
        saldo = round(saldo, 7)
        if saldo < 0.0000000:
            raise APIException(409, 'El saldo debe ser mayor a cero')
        user = User.objects(id=user_id).first()
        if not user:
            raise ModelDoesNotExist(User.__name__, user_id)
        currency = Currency.objects(id=currency_id).first()
        if not currency:
            raise ModelDoesNotExist(Currency.__name__, currency_id)
        account = Account.objects((Q(user__email=user.email) & Q(currency__name=currency.name) & Q(deleted=False))).first()
        if account:
            raise APIException(400, 'El usuario %s ya posee una cuenta %s' % (user.full_name, currency.name))
        return user, currency, saldo

    def validate(self, user_id, currency_id, saldo):
        if not user_id:
            raise MissingDataRequest('user_id')
        if len(user_id) != 24:
            raise ModelDoesNotExist(User.__name__, user_id)
        if not currency_id:
            raise MissingDataRequest('currency_id')
        if len(currency_id) != 24:
            raise ModelDoesNotExist(Currency.__name__, currency_id)
        if type(saldo) != float:
            raise APIException(409, 'Error de formato, el saldo debe ser un número decimal.')

    def get_data(self, content):
        user_id = content.get('user_id', '')
        currency_id = content.get('currency_id', '')
        saldo = content.get('saldo', 0.)
        self.validate(user_id, currency_id, saldo)
        return user_id, currency_id, saldo


class AccountApiController(Resource):

    def get(self, user_id=None):
        # Búsqueda de cuenta para transferir (validación).
        if user_id is None:
            raise APIException(404, 'Recurso no encontrado')
        account = Account.objects(user__id=user_id, deleted=False).first()
        if not account:
            raise ModelDoesNotExist(Account.__name__, user_id)
        return mongo_to_dict(account, exclude_fields=['created_at', 'updated_at']), 200

class DestinyApiController(Resource):

    def get(self, number=None):
        # Búsqueda de cuenta para transferir (validación).
        if number is None:
            raise APIException(404, 'Recurso no encontrado')
        account = Account.objects(number=number, deleted=False).first()
        if not account:
            raise ModelDoesNotExist(Account.__name__, number)
        return mongo_to_dict(account, exclude_fields=['created_at', 'updated_at']), 200
