from flask import request
from flask_restful import Resource
from models import Transfer
from models import Account
from tools import mongo_to_dict, ZenMail
from db import Q


class TransfersApiController(Resource):

    def __init__(self, mail):
        self.mail = mail

    def post(self):
        # Creación de transferencia y actualización de saldos.
        content = request.get_json()
        from_account_id = content.get('from_account_id', '')
        if not from_account_id:
            return {'message': 'Error en la solicitud'}, 400
        to_account_id = content.get('to_account_id', '')
        if not to_account_id:
            return {'message': 'Error en la solicitud'}, 400
        total = round(content.get('total', 0.), 7)
        if not total:
            return {'message': 'El total es obligatorio'}, 400
        if total < 0.0000000:
            return {'message': 'El total debe ser mayor a cero'}, 400
        from_account = Account.objects(id=from_account_id, deleted=False).first()
        if from_account is None:
            return {'message': 'La cuenta de origen no se encuentra'}, 400
        if not from_account.checkTransaction(total):
            return {'message': 'Saldo insuficiente'}, 400
        to_account = Account.objects(id=to_account_id, deleted=False).first()
        if to_account is None:
            return {'message': 'La cuenta de destino no se encuentra'}, 400
        try:
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
        except Exception as e:
            message = 'Error de servidor, vuelva a intentar más tarde. '
            message += 'Si el error persiste, contáctese con soporte.'
            return {'message': message}, 500


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
