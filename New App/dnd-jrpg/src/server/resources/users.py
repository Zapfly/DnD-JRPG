import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required

from models.users import UserModel
    
class UserRegister(Resource):
    parcer = reqparse.RequestParser()
    parcer.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parcer.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = UserRegister.parcer.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 404

        user = UserModel(**data)
        user.save_to_db()
        return_user = user.json()        

        return {"message": "User created successfully.", 'user': {'user_id': return_user['user_id'], 'username': return_user['username']}}, 201
    
    def delete(self):
        data = UserRegister.parcer.parse_args()

        user = UserModel.find_by_username(data['username'])

        if user:
            user.delete_from_db()             
            return {"message": "User deleted successfully."}, 200
           
        return {"message": "A user with that username does not exist"}, 404

    @jwt_required()
    def get(self):
        data = UserRegister.parcer.parse_args()

        user = UserModel.find_by_username_and_password(data['username'], data['password'])

        if user:
            result = user.json()
            return {"username": result["username"], "user_id": result["user_id"]}, 200
        return {"message": "That user does not exist"}, 404
