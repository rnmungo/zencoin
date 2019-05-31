from db import Document, StringField, DateTimeField
import datetime


class Currency(Document):

    name       = StringField(max_length=30)
    created_at = DateTimeField(default=datetime.datetime.today())
    updated_at = DateTimeField(default=datetime.datetime.today())
