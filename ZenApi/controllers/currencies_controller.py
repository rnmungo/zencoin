from flask import request
from flask_restful import Resource, abort
from models import Currency
from tools import mongo_to_dict
from .exceptions import (APIException,
                         MissingDataRequest,
                         ModelDoesNotExist)


class CurrenciesApiController(Resource):

    def get(self):
        currencies = Currency.objects.all()
        if not currencies.count():
            raise APIException(409, 'No hay monedas cargadas')
        dict_currencies = {}
        for i, currency in enumerate(currencies, start=1):
            dict_currencies[i] = mongo_to_dict(currency, exclude_fields=['created_at', 'updated_at'])
        return dict_currencies, 200

    def post(self):
        content = request.get_json()
        name = content.get('name', '')
        if not name:
            raise MissingDataRequest('name')
        currency = Currency.objects(name=name).first()
        if currency:
            raise APIException(400, 'La moneda ya existe')
        try:
            currency = Currency(name=name).save()
            return mongo_to_dict(currency, exclude_fields=['created_at', 'updated_at']), 200
        except Exception as e:
            abort(e.code, str(e))


class CurrencyApiController(Resource):

    def get(self, id=None):
        if id is None:
            raise APIException(404, 'Recurso no encontrado')
        if len(id) != 24:
            raise ModelDoesNotExist(Currency.__name__, id)
        currency = Currency.objects(id=id).first()
        if not currency:
            raise ModelDoesNotExist(Currency.__name__, id)
        return mongo_to_dict(currency, exclude_fields=['created_at', 'updated_at']), 200
