import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required


class Hero(Resource):
    TABLE_NAME = 'heroes'
    parser = reqparse.RequestParser()
    parser.add_argument('hero_id',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('hero_info',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    @classmethod
    def find_by_hero_id(cls, hero_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM heroes WHERE hero_id=?"
        result = cursor.execute(query, (hero_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
    
    @jwt_required()
    def put(self, hero_id):
        data = Hero.parser.parse_args()

        hero = self.find_by_hero_id(hero_id)
        updated_hero = {'hero_id': data[hero_id], 'hero_info': data["hero_info"]}

        if hero is None:
            try:
                self.insert(updated_hero)
            except:
                return {"message": "An error occured inserting the item"}, 500
        else:
            try:
                self.update(updated_hero)
            except:
                return {"message": "An error occured inserting the item"}, 500
        return updated_hero
        
    # @jwt_required()
    def post(self):
        data = Hero.parser.parse_args()
        if self.find_by_hero_id(data["hero_id"]):
            return {"message": "That hero already exists"}, 400
       
        new_hero = {'hero_id': data["hero_id"], 'hero_info': data["hero_info"]}
     
        try:
            Hero.insert(new_hero)
        except:
            return {"message": "An error occured inserting the item"}, 500

        return new_hero
    
    @classmethod
    def insert(cls, hero):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO heroes VALUES (?, ?)"
        cursor.execute(query, (hero['hero_id'], hero['hero_info']))

        connection.commit()
        connection.close()
    

        

