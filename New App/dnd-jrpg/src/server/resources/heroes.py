import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required

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
    parser.add_argument('user_id',
        type=int,
        required=True,
        help="A user id is required"
    )

    @jwt_required()
    def post(self, heroname):
        data = Hero.parser.parse_args()
        if HeroModel.find_by_user_id_and_heroname(data['user_id'], heroname):
            return {'message': "A hero with name '{}' already exists.".format(heroname)}, 404
        hero = HeroModel(**data)
        hero.save_to_db()
        return {'message': 'Hero created successfully', 'hero': hero.json()}

    @jwt_required()
    def get(self, heroname):
        data = Hero.parser.parse_args()
        hero = HeroModel.find_by_user_id_and_heroname(data['user_id'], heroname)
        if hero:
            return hero.json(), 200
        return {'message': 'Hero not found'}, 404

    @jwt_required()
    def put(self, heroname):
        data = Hero.parser.parse_args()
        hero = HeroModel.find_by_user_id_and_heroname(data['user_id'], heroname)      
        if hero is None:
            if HeroModel.find_by_user_id_and_heroname(data['user_id'], data['heroname']):
                return {'message': "A hero with name '{}' already exists.".format(data['heroname'])}, 404
            else:
                hero = HeroModel(**data)
                hero.save_to_db()
                return {'message': "Hero created successfully"}, 201
        else:
            if HeroModel.find_by_user_id_and_heroname(data['user_id'], data['heroname']):
                return {'message': "A hero with name '{}' already exists.".format(data['heroname'])}, 404
            else:
                hero.heroname = data['heroname']
                hero.atk = data['atk']
                hero.hp = data['hp']
                hero.max_hp = data['max_hp']
                hero.sprite = data['sprite']
                hero.user_id = data['user_id']              
                hero.save_to_db()
                return {'message': "Hero updated"}, 200

    @jwt_required()
    def delete(self, heroname):
        data = Hero.parser.parse_args()

        hero = HeroModel.find_by_user_id_and_heroname(data['user_id'], heroname)

        if hero:
            hero.delete_from_db()
            return{"message": "Hero deleted"}, 200
        else:
            return{"message": "That hero does not exist"}, 404

class HeroList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id',
        type=int,
        required=True,
        help="A user id is required"
    )

    def get(self):
        data = Hero.parser.parse_args()

        hero_list = HeroModel.find_all_by_user_id(data['user_id'])
        hero_list_json = {'heroes': [hero.json() for hero in hero_list]}

        if len(hero_list_json['heroes']) > 0:
            return hero_list_json, 200
        else:
            return {'message': "Either this user doesn't exist, or they have no heroes"}, 404
