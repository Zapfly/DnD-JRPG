from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, jwt_refresh_token_required
from models.users import UserModel
    

_global_parser = reqparse.RequestParser()
_global_parser.add_argument('username',
    type=str,
    required=True,
    help="This field cannot be left blank!"
)
_global_parser.add_argument('password',
    type=str,
    required=True,
    help="This field cannot be left blank!"
)

class UserRegister(Resource):
    def post(self):
        data = _global_parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}, 404

        hashedpass = UserModel.generate_hash(data['password'])
        user = UserModel(data['username'], hashedpass)
        try:
            user.save_to_db()        
            return {"message": "User '{}' created successfully.".format(data['username'])}, 201
        except:
            return {"message": "Something went wrong."}, 500

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('target',
    type=int,
    required=True,
    help="This field cannot be left blank!"
)

class User(Resource):
    @classmethod
    @jwt_required
    def get(cls):
        data = _user_parser.parse_args()

        # -1 => targets self
        if data['target'] == -1:
            user_id = get_jwt_identity()
        else:
            user_id = data['target']
        user = UserModel.find_by_id(user_id)
        if user:
            return user.json(), 200
        return {"message": "User not found."}, 404

    @classmethod
    @jwt_required
    def delete(cls):
        data = _user_parser.parse_args()

        # -1 => targets self
        if data['target'] == -1:
            user_id = get_jwt_identity()
        else:
            user_id = data['target']
        user = UserModel.find_by_id(user_id)
        if user:
            user.delete_from_db()             
            return {"message": "User deleted successfully."}, 200           
        return {"message": "User not found."}, 404

class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = _global_parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user and UserModel.verify_hash(data['password'], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        return {"message": "Invalid credentials."}, 401

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        user = get_jwt_identity()
        new_token = create_access_token(identity=user.id, fresh=False)
        return {'access_token': new_token}, 200