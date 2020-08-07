from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
import datetime

from security import authenticate, identity
from users import UserRegister
from heroes import Hero
from heroes import HeroList

app = Flask(__name__)
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1)
app.secret_key = 'jose'

api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

# api.add_resource(Level, '/level/<string:name>')
api.add_resource(Hero, '/hero')
api.add_resource(HeroList, '/heroes')
api.add_resource(UserRegister, '/new-user') #change to <integer:id>


#api.add_resource(Student, '/student/<string:name>')
 
if __name__ == '__main__':
	print("--- Starting", __file__)
	app.run(debug=True, use_reloader=True, port=5000)
# app.run(port=5000)