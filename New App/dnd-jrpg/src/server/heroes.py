import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required


class Hero(Resource):
    TABLE_NAME = 'heroes'
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
    # @jwt_required()
    # def put(self, hero_id):
    #     data = Hero.parser.parse_args()

    #     hero = self.find_by_hero_id(hero_id)
    #     updated_hero = {'hero_id': data["hero_id"], 'hero_info': data["hero_info"]}

    #     if hero is None:
    #         try:
    #             self.insert(updated_hero)
    #         except:
    #             return {"message": "An error occured inserting the item"}, 500
    #     else:
    #         try:
    #             self.update(updated_hero)
    #         except:
    #             return {"message": "An error occured inserting the item"}, 500
    #     return updated_hero

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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        user_heroes_query = "SELECT * FROM heroes WHERE username=? AND heroname=?"
        user_heroes = cursor.execute(user_heroes_query, (data["username"], data["heroname"]))
        row = user_heroes.fetchone()
        if row:
            connection.commit()
            connection.close()
            return {"message": "A hero with that name already exists"}, 400                    
        else:
            new_hero = {'username': data["username"], 'heroname': data["heroname"], 'atk': data["atk"], 'hp': data["hp"], 'max_hp': data["hp"], 'sprite': data["sprite"]}
        
            try:
                Hero.insert(new_hero)
            except:
                return {"message": "An error occured inserting the hero"}, 500
            connection.commit()
            connection.close()
            return new_hero
            
    
    @classmethod
    def insert(cls, hero):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO heroes VALUES (NULL, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (hero['username'], hero['heroname'], hero['atk'], hero['hp'], hero['max_hp'], hero['sprite']))

        connection.commit()
        connection.close()
    
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

class HeroList(Resource):
    TABLE_NAME = 'heroes'
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('heroname',
        type=str,
        help="This field cannot be left blank!"
    )

    

        

