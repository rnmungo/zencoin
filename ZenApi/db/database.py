from mongoengine import connect
from mongoengine import Document
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

connect('zen_test', host='localhost', port=27017)
