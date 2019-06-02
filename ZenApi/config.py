import os


class Development(object):

    DEBUG               = True
    SERVER_NAME         = 'localhost:9000'
    MAIL_SERVER         = 'smtp.gmail.com'
    MAIL_PORT           = 587
    MAIL_USERNAME       = 'rodrigomungo@gmail.com'
    MAIL_PASSWORD       = 'BxCLM8xter343.n'
    MAIL_USE_TLS        = True
    MAIL_USE_SSL        = False
    MAIL_DEFAULT_SENDER = 'rodrigomungo@gmail.com'


class Production(object):

    DEBUG       = True
    SERVER_NAME = 'localhost:5000'
