from .api_exception import APIException


class MissingDataRequest(APIException):

    def __init__(self, field):
        self._code = 400
        self._message = '{} es requerido'.format(field)
