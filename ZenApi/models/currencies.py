from db import Document
from db import StringField
from db import DateTimeField
from datetime import datetime

DEFAULT_CURRENCY_NAME = 'ZenCoin'


class Currency(Document):

    name       = StringField(max_length=30, required=True)
    created_at = DateTimeField(default=datetime.today())
    updated_at = DateTimeField(default=datetime.today())

    meta = {'collection': 'currencies'}
