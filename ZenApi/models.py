from werkzeug.security import generate_password_hash
import datetime
import json
import re

class Collection(object):

    def setCollection(self, collection):
        self.collection = collection


class User(Collection):

    ROLE_CUSTOMER = 'customer'
    ROLE_ADMIN = 'admin'

    def __init__(self, collection, **kwargs):
        self.setCollection(collection)
        self.setObject(**kwargs)

    def setObject(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.created_at = kwargs.get('created_at', None)
        self.updated_at = kwargs.get('updated_at', None)
        self.role = self.ROLE_ADMIN if kwargs.get('is_staff', 0) else self.ROLE_CUSTOMER

    def is_valid(self):
        if not self.name:
            return False
        if not self.email:
            return False
        if not self.password:
            return False
        if not re.match('^[a-zA-Z0-9]{3,30}$', self.name):
            return False
        if not re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', self.email):
            return False
        return True

    def save(self):
        if not self.is_valid():
            raise Exception(u"Datos inválidos")
        user = self.collection.find_one({"$or": [{"name": self.name, "email": self.email}]})
        if user is not None:
            if user.name == self.name:
                raise Exception("Nombre de usuario en uso")
            elif user.email == self.email:
                raise Exception("E-mail en uso")
        else:
            user = {}
        user['name'] = self.name
        user['email'] = self.email
        user['password'] = generate_password_hash(self.password)
        user['created_at'] = datetime.datetime.today()
        user['updated_at'] = datetime.datetime.today()
        user['role'] = self.role
        self.collection.save(user)

    def toDICT(self):
        return {
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
