from flask import Flask
from flask_restful import Api
from flask_mail import Mail
from config import Production as Config
from controllers import *
from mongoengine import connect
import json


class ZenApi(Api):

    def handle_error(self, e):
        return json.dumps({'message': str(e)}), e.code

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
api = ZenApi(app)

connect(app.config['MONGODB_DB'], host=app.config['MONGODB_HOST'], port=app.config['MONGODB_PORT'])

api.add_resource(UsersApiController, '/users', resource_class_kwargs={'mail': mail})
api.add_resource(UserApiController, '/users/<string:id>')
api.add_resource(LoginApiController, '/auth')
api.add_resource(CurrenciesApiController, '/currencies')
api.add_resource(CurrencyApiController, '/currencies/<string:id>')
api.add_resource(AccountsApiController, '/accounts')
api.add_resource(AccountApiController, '/accounts/<string:user_id>')
api.add_resource(TransfersApiController, '/transfers', resource_class_kwargs={'mail': mail})
api.add_resource(TransferApiController, '/transfers/<string:id>')
api.add_resource(MovementsApiController, '/movements/<string:id>')
api.add_resource(ConversionApiController, '/conversions')
api.add_resource(ConversionsApiController, '/conversions/<string:currency_id>')
app.run()
