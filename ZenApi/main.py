from flask import Flask
from flask_restful import Api
from config import Development
from controllers import *

app = Flask(__name__)
app.config.from_object(Development)

api = Api(app)
api.add_resource(UsersApiController, '/users')
api.add_resource(UserApiController, '/users/<string:id>')
api.add_resource(LoginApiController, '/auth')
app.run()
