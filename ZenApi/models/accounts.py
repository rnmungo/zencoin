from db import Document, StringField, ReferenceField, DecimalField, DateTimeField
from .users import User
from .currencies import Currency
import datetime


class Account(Document):

    number     = StringField(max_length=30, required=True, unique=True)
    user       = ReferenceField(User)
    saldo      = DecimalField(min_value=0., precision=5, default=0.)
    currency   = ReferenceField(Currency)
    created_at = DateTimeField(default=datetime.datetime.today())
    updated_at = DateTimeField(default=datetime.datetime.today())
    deleted_at = DateTimeField()
