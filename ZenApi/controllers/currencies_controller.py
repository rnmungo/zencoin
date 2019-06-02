from flask import request
from flask_restful import Resource
from models import Currency
from tools import mongo_to_dict


class CurrenciesApiController(Resource):

    def get(self):
        currencies = Currency.objects.all()
        dict_currencies = {}
        for i, currency in enumerate(currencies, start=1):
            dict_currencies[i] = mongo_to_dict(currency, exclude_fields=['created_at', 'updated_at'])
        return dict_currencies, 200

    def post(self):
        content = request.get_json()
        name = content.get('name', '')
        if not name:
            return {'message', 'El nombre es requerido'}, 400
        currency = Currency.objects(name=name).first()
        if currency is not None:
            return {'message': 'La moneda ya existe'}, 400
        try:
            currency = Currency(name=name).save()
            return mongo_to_dict(currency, exclude_fields=['created_at', 'updated_at']), 200
        except Exception:
            return {'message': 'Error al guardar la moneda'}, 400


class CurrencyApiController(Resource):

    def get(self, id=None):
        if id is None:
            return {'message': 'Error en la solicitud'}, 400
        currency = Currency.objects(id=id).first()
        if currency is None:
            return {'message': 'La moneda no existe'}, 400
        return mongo_to_dict(currency, exclude_fields=['created_at', 'updated_at']), 200
