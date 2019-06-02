from db import Document
from db import StringField
from db import DateTimeField
import datetime

DEFAULT_CURRENCY_NAME = 'ZenCoin'


class Currency(Document):

    name       = StringField(max_length=30, required=True)
    created_at = DateTimeField(default=datetime.datetime.today())
    updated_at = DateTimeField(default=datetime.datetime.today())

    meta = {'collection': 'currencies'}
