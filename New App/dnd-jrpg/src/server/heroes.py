import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required


class Hero(Resource):
    TABLE_NAME = 'heroes'
    parser = reqparse.RequestParser()
    # parser.add_argument('hero_id',
    #     type=int,
    #     required=True,
    #     help="This field cannot be left blank!"
    # )
    parser.add_argument('user_id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('name',
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
    # parser.add_argument('hero_info',
    #     type=str,
    #     required=True,
    #     help="This field cannot be left blank!"
    # )

    # @classmethod
    # def find_by_hero_id(cls, hero_id):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "SELECT rowid, * FROM heroes WHERE hero_id=?"
    #     result = cursor.execute(query, (hero_id,))
    #     row = result.fetchone()
    #     if row:
    #         hero = cls(*row)
    #     else:
    #         hero = None

    #     connection.close()
    #     return hero
    
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
        
    # @jwt_required()
    # def post(self):
    #     data = Hero.parser.parse_args()
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     # if self.find_by_hero_id(data["hero_id"]):
    #     #     return {"message": "That hero already exists"}, 400
    #     search_query = "SELECT * FROM heroes WHERE hero_id=?"
    #     result = cursor.execute(search_query, (data["hero_id"],))
    #     row = result.fetchone()
    #     if row:
    #         connection.commit()
    #         connection.close()
    #         return {"message": "That hero already exists"}, 400     
    #     else:
    #         new_hero = {'hero_id': data["hero_id"], 'user_id': data["user_id"], 'name': data["hero_info"]}
        
    #         try:
    #             Hero.insert(new_hero)
    #         except:
    #             return {"message": "An error occured inserting the hero"}, 500
    #         connection.commit()
    #         connection.close()
    #         return new_hero

    @jwt_required()
    def post(self):
        data = Hero.parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        user_heroes_query = "SELECT * FROM heroes WHERE user_id=? AND name=?"
        user_heroes = cursor.execute(user_heroes_query, (data["user_id"], data["name"]))
        row = user_heroes.fetchone()
        if row:
            connection.commit()
            connection.close()
            return {"message": "A hero with that name already exists"}, 400                    
        else:
            # new_hero = {'hero_id': data["hero_id"], 'user_id': data["user_id"], 'hero_info': data["hero_info"]}
            new_hero = {'user_id': data["user_id"], 'name': data["name"], 'atk': data["atk"], 'hp': data["hp"], 'max_hp': data["hp"], 'sprite': data["sprite"]}
        
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
        cursor.execute(query, (hero['user_id'], hero['name'], hero['atk'], hero['hp'], hero['max_hp'], hero['sprite']))

        connection.commit()
        connection.close()
    
    @jwt_required()
    def delete(self):
        data = Hero.parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        user_heroes_query = "SELECT * FROM heroes WHERE user_id=? AND name=?"
        user_heroes = cursor.execute(user_heroes_query, (data["user_id"], data["name"]))
        row = user_heroes.fetchone()
        if row:
            delete_query = "DELETE FROM heroes WHERE user_id=? AND name=?"
            cursor.execute(delete_query, (data["user_id"], data["name"]))
            connection.commit()
            connection.close()      
            return{"message": "Hero deleted"}, 202
        else:
            connection.commit()
            connection.close()
            return{"message": "That hero does not exist"}, 400

        # if self.find_by_hero_id(data["hero_id"]):
        #     delete_query = "DELETE FROM heroes WHERE hero_id=?"
        #     cursor.execute(delete_query, (data["hero_id"],))
        #     connection.commit()
        #     connection.close()      
        #     return{"message": "Hero deleted"}, 202
        # else:
        #     connection.commit()
        #     connection.close()
        #     return{"message": "That hero does not exist"}, 400

        

