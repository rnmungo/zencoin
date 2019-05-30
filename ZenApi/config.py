import os


class Development(object):

    DEBUG = True
    SERVER_NAME = 'localhost:8000'
    MONGO_URI = 'mongodb://localhost:27017/zen_test'


class Production(object):

    DEBUG = True
    SERVER_NAME = 'localhost:5000'
    MONGO_URI = 'mongodb://localhost:27017/zen'
