from mongoengine import connect
from mongoengine import Document
from mongoengine import EmbeddedDocument
from mongoengine import StringField
from mongoengine import BooleanField
from mongoengine import DateTimeField
from mongoengine import DecimalField
from mongoengine import EmailField
from mongoengine import ReferenceField
from mongoengine import ListField
from mongoengine import ComplexDateTimeField
from mongoengine import DictField
from mongoengine import EmbeddedDocumentField
from mongoengine import IntField
from mongoengine import FloatField
from mongoengine import ObjectIdField
from mongoengine.queryset.visitor import Q

connect('zen_test', host='localhost', port=27017)
