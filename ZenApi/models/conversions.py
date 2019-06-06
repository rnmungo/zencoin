from db import Document
from db import DictField
from db import FloatField
from db import DateTimeField
from datetime import datetime


class Conversion(Document):

    from_currency = DictField()
    to_currency   = DictField()
    rate          = FloatField()
    created_at    = DateTimeField(default=datetime.today())
    updated_at    = DateTimeField(default=datetime.today())

    meta = {'collection': 'conversions'}
