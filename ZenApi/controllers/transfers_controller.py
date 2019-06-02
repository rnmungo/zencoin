from flask import request
from flask_restful import Resource, abort
from models import Transfer
from models import Account
from tools import mongo_to_dict, ZenMail
from db import Q
from .exceptions import (APIException,
                         MissingDataRequest,
                         ResourceDoesNotExist)


class TransfersApiController(Resource):

    def __init__(self, mail):
        self.mail = mail

    def post(self):
        # Creación de transferencia y actualización de saldos.
        try:
            from_account_id, to_account_id, total = self.defragment_json(request.get_json())
            self.validate_request(from_account_id, to_account_id, total)
            from_account, to_account, total = self.get_data(from_account_id, to_account_id, total)
            transfer = Transfer(
                from_account=mongo_to_dict(from_account, exclude_fields=['created_at', 'updated_at', 'saldo']),
                to_account=mongo_to_dict(to_account, exclude_fields=['created_at', 'updated_at', 'saldo']),
                total=total
            ).save()
            # TO DO: Rollback si falla el guardado de las cuentas.
            from_account.saldo -= total
            from_account.save()
            to_account.saldo += total
            to_account.save()
            # Envío de e-mail de transferencia.
            ZenMail.send_transfer_message(self.mail, from_account, to_account, transfer.total)
            return mongo_to_dict(transfer, exclude_fields=['updated_at']), 200
        except APIException as e:
            abort(e.code, message=str(e))

    def defragment_json(self, content):
        from_account_id = content.get('from_account_id', '')
        to_account_id = content.get('to_account_id', '')
        total = content.get('total', None)
        return from_account_id, to_account_id, total

    def validate_request(self, from_account_id, to_account_id, total):
        if not from_account_id:
            raise MissingDataRequest('from_account_id')
        if not to_account_id:
            raise MissingDataRequest('to_account_id')
        if not total:
            raise MissingDataRequest('total')
        if type(total) != float:
            raise APIException(409, 'Error de formato, el total debe ser un número decimal.')

    def get_data(self, from_account_id, to_account_id, total):
        total = round(total, 7)
        if total < 0.0000000:
            raise APIException(409, 'El total debe ser mayor a cero')
        from_account = Account.objects(id=from_account_id, deleted=False).first()
        if not from_account:
            raise ResourceDoesNotExist(Account.__name__, from_account_id)
        to_account = Account.objects(id=to_account_id, deleted=False).first()
        if not to_account:
            raise ResourceDoesNotExist(Account.__name__, to_account_id)
        if not from_account.checkTransaction(total):
            raise APIException(409, 'Saldo insuficiente')
        return from_account, to_account, total


class MovementsApiController(Resource):

    def get(self, id=None):
        if id is None:
            return {'message': 'Error en la solicitud'}, 400
        # Toma las transferencias in/out de la cuenta.
        transfers = Transfer.objects(Q(from_account__id=id) | Q(to_account__id=id)).order_by('-created_at')
        if not transfers.count():
            return {'message': 'No hay transferencias'}, 400
        dict_transfers = {}
        for i, transfer in enumerate(transfers, start=1):
            dict_transfers[i] = mongo_to_dict(transfer, exclude_fields=['updated_at'])
        return dict_transfers, 200


class TransferApiController(Resource):

    def get(self, id=None):
        if id is None:
            return {'message': 'Error en la solicitud'}, 400
        transfer = Transfer.objects(id=id).first()
        if transfer is None:
            return {'message': 'La transferencia no existe'}, 400
        return mongo_to_dict(transfer, exclude_fields=['updated_at']), 200
