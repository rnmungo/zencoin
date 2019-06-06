from db import Document
from db import FloatField
from db import DateTimeField
from db import IntField
from db import BooleanField
from db import DictField
from datetime import datetime


class Account(Document):

    number     = IntField(min_value=1)
    user       = DictField()
    saldo      = FloatField(min_value=0., default=0.)
    currency   = DictField()
    created_at = DateTimeField(default=datetime.today())
    updated_at = DateTimeField(default=datetime.today())
    deleted    = BooleanField(default=False)

    meta = {
        'collection': 'accounts'
    }

    def checkTransaction(self, total):
        return self.saldo - total >= 0.00
