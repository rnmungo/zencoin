

class Config(object):

    DEBUG               = False
    TESTING             = False
    THREADED            = True
    MAIL_SERVER         = 'smtp.gmail.com'
    MAIL_PORT           = 587
    MAIL_USERNAME       = 'zencoin.soporte2019@gmail.com'
    MAIL_PASSWORD       = 'zEn345.,coIn#'
    MAIL_USE_TLS        = True
    MAIL_USE_SSL        = False
    MAIL_DEFAULT_SENDER = 'zencoin.soporte2019@gmail.com'


class Development(Config):

    DEBUG        = True
    SERVER_NAME  = 'localhost:9000'
    MONGODB_DB   = 'zen_dev'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017


class Production(Config):

    SERVER_NAME  = 'localhost:5000'
    MONGODB_DB   = 'zen'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017


class Testing(Config):

    TESTING = True
