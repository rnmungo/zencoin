from db import Document
from db import StringField
from db import EmailField
from db import DateTimeField
from datetime import datetime


class User(Document):

    email      = EmailField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name  = StringField(max_length=50)
    password   = StringField(required=True)
    created_at = DateTimeField(default=datetime.today())
    updated_at = DateTimeField(default=datetime.today())
    role       = StringField(max_length=20)

    meta = {'collection': 'users'}

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    