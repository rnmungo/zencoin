from .api_exception import APIException


class MissingDataRequest(APIException):

    def __init__(self, field):
        message = '{} es requerido'.format(field)
        super(APIException, self).__init__(400, message)
