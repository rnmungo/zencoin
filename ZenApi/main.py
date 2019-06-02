from flask import Flask
from flask_restful import Api
from flask_mail import Mail
from config import Development
from controllers import *

app = Flask(__name__)
app.config.from_object(Development)
mail = Mail(app)
api = Api(app)
api.add_resource(UsersApiController, '/users', resource_class_kwargs={'mail': mail})
api.add_resource(UserApiController, '/users/<string:id>')
api.add_resource(LoginApiController, '/auth')
api.add_resource(CurrenciesApiController, '/currencies')
api.add_resource(CurrencyApiController, '/currencies/<string:id>')
api.add_resource(AccountsApiController, '/accounts', resource_class_kwargs={'mail': mail})
api.add_resource(AccountApiController, '/accounts/<int:number>')
api.add_resource(TransfersApiController, '/transfers', resource_class_kwargs={'mail': mail})
api.add_resource(TransferApiController, '/transfers/<string:id>')
api.add_resource(MovementsApiController, '/movements/<string:id>', )
# threaded permite correr cada solicitud en un hilo separado.
app.run(threaded=True)
