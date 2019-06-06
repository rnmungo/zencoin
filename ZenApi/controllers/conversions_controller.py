from flask import request
from flask_restful import Resource, abort
from models import Conversion, Currency
from tools import mongo_to_dict
from .exceptions import (APIException,
                         MissingDataRequest,
                         ModelDoesNotExist)


class ConversionsApiController(Resource):

    def get(self, id=None):
        if id is None:
            raise APIException(404, 'Recurso no encontrado')
        if len(id) != 24:
            raise ModelDoesNotExist(Currency.__name__, id)
        conversions = Conversion.objects(from_currency__id=id)
        if not conversions.count():
            raise APIException(409, 'No hay conversiones cargadas')
        dict_conversions = {}
        for i, conversion in enumerate(conversions, start=1):
            dict_conversions[i] = mongo_to_dict(conversion, exclude_fields=['created_at', 'updated_at'])
        return dict_conversions, 200


class ConversionApiController(Resource):

    def post(self):
        # Registro de Conversiones
        from_currency_id, to_currency_id, rate = self.get_data(request.get_json())
        self.validate(from_currency_id, to_currency_id, rate)
        from_currency, to_currency = self.get_models(from_currency_id, to_currency_id)
        try:
            conversion = Conversion(
                from_currency=mongo_to_dict(from_currency,
                    exclude_fields=['created_at', 'updated_at']),
                to_currency=mongo_to_dict(to_currency,
                    exclude_fields=['created_at', 'updated_at']),
                rate=rate
            ).save()
            return mongo_to_dict(conversion, exclude_fields=['created_at', 'updated_at'])
        except APIException as e:
            abort(e.code, str(e))

    def get_models(self, from_currency_id, to_currency_id):
        from_currency = Currency.objects(id=from_currency_id).first()
        if not from_currency:
            raise ModelDoesNotExist(Currency.__name__, from_currency_id)
        to_currency = Currency.objects(id=to_currency_id).first()
        if not to_currency:
            raise ModelDoesNotExist(Currency.__name__, to_currency_id)
        return from_currency, to_currency

    def validate(self, from_currency_id, to_currency_id, rate):
        if not from_currency_id:
            raise MissingDataRequest('from_currency_id')
        if len(from_currency_id) != 24:
            raise ModelDoesNotExist(Currency.__name__, from_currency_id)
        if not to_currency_id:
            raise MissingDataRequest('to_currency_id')
        if len(to_currency_id) != 24:
            raise ModelDoesNotExist(Currency.__name__, to_currency_id)
        if not rate:
            raise MissingDataRequest('rate')
        if type(rate) != float:
            raise APIException(409, 'Error de formato, el monto de conversión debe ser un número decimal.')
        rate = round(rate, 7)
        if rate < 0.0000000:
            raise APIException(409, 'El monto de conversión debe ser mayor a cero')

    def get_data(self, content):
        from_currency_id = content.get('from_currency_id', '')
        to_currency_id   = content.get('to_currency_id', '')
        rate             = content.get('rate', None)
        return from_currency_id, to_currency_id, rate