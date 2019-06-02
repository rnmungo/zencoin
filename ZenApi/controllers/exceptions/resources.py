from .api_exception import APIException


class ResourceDoesNotExist(APIException):

    def __init__(self, model_name, id):
        message = 'Recurso {} {} no encontrado'.format(model_name.title(), id)
        super(APIException, self).__init__(404, message)
