from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import datetime
from db import db

from security import authenticate, identity
from resources.users import UserRegister
from resources.heroes import Hero, HeroList
from resources.levels import Level, LevelList
from resources.monsters import Monster

app = Flask(__name__)
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'jose'

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Level, '/level')
api.add_resource(LevelList, '/levels')
api.add_resource(Hero, '/hero/<string:heroname>')
api.add_resource(HeroList, '/heroes')
api.add_resource(Monster, '/monster')
api.add_resource(UserRegister, '/user') #change to <integer:id>


#api.add_resource(Student, '/student/<string:name>')
 
if __name__ == '__main__':
	print("--- Starting", __file__)
	db.init_app(app)
	app.run(debug=True, use_reloader=True, port=5000)
