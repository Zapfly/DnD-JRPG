import sqlite3
from flask_restful import Resource, reqparse

class User:
    TABLE_NAME = 'users'
    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
    

    

    @classmethod
    def find_by_id(cls, user_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = " SELECT * FROM users WHERE user_id=?"
        result = cursor.execute(query, (user_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
    
class UserRegister(Resource):
    TABLE_NAME = 'users'
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

        if User.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400            

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
    
    def delete(self):
        data = UserRegister.parcer.parse_args()

        if User.find_by_username(data['username']) == False:
            return {"message": "A user with that username does not exist"}, 400     

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM users WHERE username=?"
        cursor.execute(query, (data['username'],))

        connection.commit()
        connection.close()

        return {"message": "User deleted successfully."}, 202
 
