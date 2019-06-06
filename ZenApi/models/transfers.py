from db import Document
from db import DateTimeField
from db import FloatField
from db import DictField
from datetime import datetime


class Transfer(Document):

    created_at   = DateTimeField(default=datetime.today())
    updated_at   = DateTimeField(default=datetime.today())
    from_account = DictField()
    to_account   = DictField()
    total        = FloatField()

    meta = {'collection': 'transfers'}
