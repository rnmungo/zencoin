import os


class Development(object):

    DEBUG = True
    SERVER_NAME = 'localhost:9000'


class Production(object):

    DEBUG = True
    SERVER_NAME = 'localhost:5000'
