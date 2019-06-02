from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from models import Account, User, Currency
from tools import mongo_to_dict


class AccountsApiController(Resource):

    def post(self):
        # Creación de cuenta.
        content = request.get_json()
        user_id = content.get('user_id', '')
        if not user_id:
            return {'message': 'Error en la solicitud'}, 400
        currency_id = content.get('currency_id', '')
        if not currency_id:
            return {'message': 'Error en la solicitud'}, 400
        saldo = round(content.get('saldo', 0.), 7)
        if saldo < 0.0000000:
            return {'message': 'El saldo no puede ser negativo'}, 400
        user = User.objects(id=user_id).first()
        if user is None:
            return {'message': 'Usuario inconsistente o no existe'}, 400
        currency = Currency.objects(id=currency_id).first()
        if currency is None:
            return {'message': 'Moneda inconsistente o no existe'}, 400
        account = Account.objects(user_id=user, currency_id=currency, deleted=False).first()
        if account is not None:
            return {'message': 'El usuario %s ya posee una cuenta %s' % (user.full_name, currency.name)}, 400
        try:
            account = Account(
                user=mongo_to_dict(user, exclude_fields=['created_at', 'updated_at', 'password']),
                currency=mongo_to_dict(currency, exclude_fields=['created_at', 'updated_at']),
                saldo=saldo,
                number=Account.objects.count()+1
            ).save()
            return mongo_to_dict(account, exclude_fields=['created_at', 'updated_at']), 200
        except Exception as e:
            return {'message': str(e)}, 400


class AccountApiController(Resource):

    def get(self, number=None):
        # Búsqueda de cuenta para transferir (validación).
        if id is None:
            return {'message': 'Error en la solicitud'}, 400
        account = Account.objects(number=number, deleted=False).first()
        if account is None:
            return {'message': 'Cuenta no encontrada'}, 400
        return mongo_to_dict(account, exclude_fields=['created_at', 'updated_at']), 200
