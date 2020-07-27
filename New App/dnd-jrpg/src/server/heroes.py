import sqlite3
from flask_restful import Resource, reqparse

class Hero:
    TABLE_NAME = 'heroes'
    def __init__(self, hero_id, user_id, hero_info):
        self.hero_id = hero_id
        self.user_id = user_id
        self.hero_info = hero_info

    @classmethod
    def find_by_hero_id(cls, hero_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE hero_id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
    
    @jwt_required()
    def put(self, hero_id):
        data = Item.parcer.parse_args()

        hero = self.find_by_hero_id(hero_id)
        updated_hero = {'hero_id': hero_id, 'user_id': data['user_id'], 'hero_info': data["hero_info"]}

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

