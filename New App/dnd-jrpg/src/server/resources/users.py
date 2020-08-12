import sqlite3
from flask_restful import Resource, reqparse
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
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()        

        return {"message": "User created successfully.", 'user': user.json()}, 201
    
    def delete(self):
        data = UserRegister.parcer.parse_args()

        user = UserModel.find_by_username(data['username'])

        if user:
            user.delete_from_db()             
            return {"message": "User deleted successfully."}, 200
           
        return {"message": "A user with that username does not exist"}, 400 

    # def get(self):
    #     data = UserRegister.parcer.parse_args()

    #     if User.find_by_username(data['username']) == False:
    #         return {"message": "A user with that username does not exist"}, 400     

    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "SELECT FROM users WHERE username=?"
    #     cursor.execute(query, (data['username'],))




 

