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
    parser.add_argument('new_heroname',
        type=str,
        help="This field cannot be left blank!"
    )
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
        if HeroModel.find_by_username_and_heroname(data['username'], data['heroname']):
            return {'message': "A hero with name '{}' already exists.".format(data['heroname'])}, 400


        hero = HeroModel(**data)
        hero.save_to_db()
        return {'message': 'Hero created successfully'}

        # user_heroes_query = "SELECT * FROM heroes WHERE username=? AND heroname=?"
        # user_heroes = cursor.execute(user_heroes_query, (data["username"], data["heroname"]))
        # row = user_heroes.fetchone()
        # if row:
        #     connection.commit()
        #     connection.close()
        #     return {"message": "A hero with that name already exists"}, 400                    
        # else:
        #     new_hero = {'username': data["username"], 'heroname': data["heroname"], 'atk': data["atk"], 'hp': data["hp"], 'max_hp': data["hp"], 'sprite': data["sprite"]}
        
        #     try:
        #         Hero.insert(new_hero)
        #     except:
        #         return {"message": "An error occured inserting the hero"}, 500
        #     connection.commit()
        #     connection.close()
        #     return new_hero
            
    
    @jwt_required()
    def delete(self):
        data = Hero.parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        user_heroes_query = "SELECT * FROM heroes WHERE username=? AND heroname=?"
        user_heroes = cursor.execute(user_heroes_query, (data["username"], data["heroname"]))
        row = user_heroes.fetchone()
        if row:
            delete_query = "DELETE FROM heroes WHERE username=? AND heroname=?"
            cursor.execute(delete_query, (data["username"], data["heroname"]))
            connection.commit()
            connection.close()      
            return{"message": "Hero deleted"}, 200
        else:
            connection.commit()
            connection.close()
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

    

        

