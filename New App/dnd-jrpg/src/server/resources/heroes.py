import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required

from models.heroes import HeroModel
from models.users import UserModel

class Hero(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        # required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('heroname',
        type=str,
        # required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('atk',
        type=float,
        # required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('hp',
        type=float,
        # required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('max_hp',
        type=float,
        # required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('sprite',
        # required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('user_id',
        type=int,
        # required=True,
        help="A user id is required"
    )


    @jwt_required()
    def put(self, heroname):
        data = Hero.parser.parse_args()

        hero = HeroModel.find_by_user_id_and_heroname(data['user_id'], heroname)
       

        if hero is None:
            if HeroModel.find_by_user_id_and_heroname(data['user_id'], data['heroname']):
                return {'message': "A hero with name '{}' already exists.".format(data['heroname'])}, 400
            else:
                hero = HeroModel(**data)
                hero.save_to_db()
                return {'message': "Hero created successfully"}
        else:
            if HeroModel.find_by_user_id_and_heroname(data['user_id'], data['heroname']):
                return {'message': "A hero with name '{}' already exists.".format(data['heroname'])}, 400
            else:
                # for item in data:
                #     print(f'{item} = {hero.json()[item]}')
                # hero[f'{item}'] = data[f'{item}']
                hero.heroname = data['heroname']
                hero.atk = data['atk']
                hero.hp = data['hp']
                hero.max_hp = data['max_hp']
                hero.sprite = data['sprite']
                hero.user_id = data['user_id']
                
                hero.save_to_db()
                return {'message': "Hero updated"}


    @jwt_required()
    def post(self, heroname):
        data = Hero.parser.parse_args()
        if HeroModel.find_by_user_id_and_heroname(data['user_id'], heroname):
            return {'message': "A hero with name '{}' already exists.".format(heroname)}, 400


        hero = HeroModel(**data)
        hero.save_to_db()
        return {'message': 'Hero created successfully', 'hero': hero.json()}

    @jwt_required()
    def get(self, heroname):
        data = Hero.parser.parse_args()
        hero = HeroModel.find_by_user_id_and_heroname(data['user_id'], heroname)
        if hero:
            return hero.json()
        return {'message': 'Hero not found'}, 404


    @jwt_required()
    def delete(self, heroname):
        data = Hero.parser.parse_args()

        hero = HeroModel.find_by_user_id_and_heroname(data['user_id'], heroname)

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