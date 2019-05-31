from db import Document, BooleanField, DateTimeField, ReferenceField, DecimalField
from .users import User
import datetime


class Transfers(Document):

    state      = BooleanField(default=0)
    created_at = DateTimeField(default=datetime.datetime.today())
    updated_at = DateTimeField(default=datetime.datetime.today())
    from_user  = ReferenceField(User)
    to_user    = ReferenceField(User)
    total      = DecimalField(min_value=0., precision=5)
