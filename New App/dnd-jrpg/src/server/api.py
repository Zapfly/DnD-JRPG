from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import datetime
from db import db

from resources.users import UserRegister, User, UserLogin, TokenRefresh
from resources.heroes import Hero, HeroList
from resources.levels import Level, LevelList
from resources.monsters import Monster

app = Flask(__name__)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=30)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'jose'

api = Api(app)
CORS(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)

api.add_resource(Level, '/level')
api.add_resource(LevelList, '/levels')
api.add_resource(Hero, '/hero/<string:heroname>')
api.add_resource(HeroList, '/heroes')
api.add_resource(Monster, '/monster')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')

#api.add_resource(Student, '/student/<string:name>')
 
if __name__ == '__main__':
	print("--- Starting", __file__)
	db.init_app(app)
	app.run(debug=True, use_reloader=True, port=5000)
