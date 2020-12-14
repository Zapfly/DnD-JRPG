import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, fresh_jwt_required, get_jwt_identity

from models.heroes import HeroModel


class Hero(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('heroname',
        type=str
    )
    parser.add_argument('atk',
        type=float
    )
    parser.add_argument('hp',
        type=float   
    )
    parser.add_argument('max_hp',
        type=float
    )
    parser.add_argument('sprite',
        type=str
    )

    @jwt_required
    def post(self, heroname):
        data = Hero.parser.parse_args()
        user_id = get_jwt_identity()

        if HeroModel.find_by_user_id_and_heroname(user_id, heroname):
            return {'message': "A hero with name '{}' already exists.".format(heroname)}, 404

        hero = HeroModel(heroname, data['atk'], data['hp'], data['max_hp'], data['sprite'], user_id)
        hero.save_to_db()

        return {'message': 'Hero created successfully', 'hero': hero.json()}

    @jwt_required
    def get(self, heroname):
        user_id = get_jwt_identity()
        hero = HeroModel.find_by_user_id_and_heroname(user_id, heroname)

        if hero:
            return hero.json(), 200
        return {'message': 'Hero not found'}, 404

    @jwt_required
    def put(self, heroname):
        data = Hero.parser.parse_args()
        user_id = get_jwt_identity()
        hero = HeroModel.find_by_user_id_and_heroname(user_id, heroname) 

        if hero is None:
            if HeroModel.find_by_user_id_and_heroname(user_id, data['heroname']):
                return {'message': "A hero with name '{}' already exists.".format(data['heroname'])}, 404
            else:
                hero = HeroModel(data['heroname'], data['atk'], data['hp'], data['max_hp'], data['sprite'], user_id)
                hero.save_to_db()
                return {'message': "Hero created successfully"}, 201
        else:
            if HeroModel.find_by_user_id_and_heroname(user_id, data['heroname']):
                return {'message': "A hero with name '{}' already exists.".format(data['heroname'])}, 404
            else:
                hero.heroname = data['heroname']
                hero.atk = data['atk']
                hero.hp = data['hp']
                hero.max_hp = data['max_hp']
                hero.sprite = data['sprite']
                hero.user_id = user_id              
                hero.save_to_db()
                return {'message': "Hero updated"}, 200

    @fresh_jwt_required
    def delete(self, heroname):     
        user_id = get_jwt_identity()
        hero = HeroModel.find_by_user_id_and_heroname(user_id, heroname)

        if hero:
            hero.delete_from_db()
            return{"message": "Hero deleted"}, 200
        else:
            return{"message": "That hero does not exist"}, 404

class HeroList(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        hero_list = HeroModel.find_all_by_user_id(user_id)
        hero_list_json = {'heroes': [hero.json() for hero in hero_list]}

        if len(hero_list_json['heroes']) > 0:
            return hero_list_json, 200
        else:
            return {'message': "Either this user doesn't exist, or they have no heroes"}, 404
