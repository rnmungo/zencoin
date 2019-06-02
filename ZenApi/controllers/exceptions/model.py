from .api_exception import APIException


class ModelDoesNotExist(APIException):

    def __init__(self, model_name, id):
        self._code = 404
        self._message = 'Modelo {} {} no encontrado'.format(model_name.title(), id)
