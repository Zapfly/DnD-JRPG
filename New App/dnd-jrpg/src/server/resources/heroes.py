import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required

from models.heroes import HeroModel
from models.users import UserModel

class Hero(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('heroname',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('atk',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('hp',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('max_hp',
        type=float,
        # required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('sprite',
        required=True,
        help="This field cannot be left blank!"
    ) 
    # parser.add_argument('new_heroname',
    #     type=str,
    #     help="This field cannot be left blank!"
    # )
    parser.add_argument('user_id', 
        type=int,
        required=True,
        help="A user id is required"
    )


    @jwt_required()
    def put(self):
        data = Hero.parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        user_heroes_query = "SELECT * FROM heroes WHERE username=? AND heroname=?"
        user_heroes = cursor.execute(user_heroes_query, (data["username"], data["heroname"]))
        row = user_heroes.fetchone()
        if row:
            update_query = "UPDATE heroes SET heroname=?, atk=?, hp=?, max_hp=?, sprite=? WHERE username=? AND heroname=?"
            update_data = (data["new_heroname"], data["atk"], data["hp"], data["max_hp"], data["sprite"], data["username"], data["heroname"],)
            cursor.execute(update_query, update_data )
            connection.commit()
            connection.close()      
            return{"message": "Hero updated", "hero":f"{update_data}"}, 200
        else:
            connection.commit()
            connection.close()
            return{"message": "That hero does not exist"}, 400

        
    @jwt_required()
    def post(self):
        data = Hero.parser.parse_args()
        if HeroModel.find_by_user_id_and_heroname(data['user_id'], data['heroname']):
            return {'message': "A hero with name '{}' already exists.".format(data['heroname'])}, 400


        hero = HeroModel(**data)
        hero.save_to_db()
        return {'message': 'Hero created successfully'}
            
    
    @jwt_required()
    def delete(self):
        data = Hero.parser.parse_args()

        hero = HeroModel.find_by_user_id_and_heroname(data['user_id'], data['heroname'])

        if hero:
            hero.delete_from_db()
            return{"message": "Hero deleted"}, 200
        else:
            return{"message": "That hero does not exist"}, 400



# class HeroList(Resource):
#     TABLE_NAME = 'heroes'
#     parser = reqparse.RequestParser()
#     parser.add_argument('username',
#         type=str,
#         required=True,
#         help="This field cannot be left blank!"
#     )
#     parser.add_argument('heroname',
#         type=str,
#         help="This field cannot be left blank!"
#     )

    

        

