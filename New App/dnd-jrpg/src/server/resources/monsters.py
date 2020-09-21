from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, fresh_jwt_required

from models.monsters import MonsterModel


class Monster(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('monstername',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('atk',
        type=int
    )
    parser.add_argument('hp',
        type=int
    )
    parser.add_argument('max_hp',
        type=int
    )
    parser.add_argument('sprite',
        type=str
    )
    parser.add_argument('levelname',
        type=str,
        required=True,
        help="Every monster must be assigned to a level!"
    )
    parser.add_argument('old_monstername',
        type=str
    )

    @fresh_jwt_required
    def post(self):
        data = Monster.parser.parse_args()

        if MonsterModel.find_by_levelname_and_monstername(data['levelname'], data['monstername']):
            return {'message': "A monster with name '{}' already exists in level '{}'.".format(data['monstername'], data['levelname'])}, 404
        
        monster = MonsterModel(data['monstername'], data['atk'], data['hp'], data['max_hp'], data['sprite'], data['levelname'])
        try:
            monster.save_to_db()
        except:
            return {'message': "An error occurred creating the monster."}, 500

        return monster.json(), 201

    @jwt_required
    def get(self):
        data = Monster.parser.parse_args()

        monster = MonsterModel.find_by_levelname_and_monstername(data['levelname'], data['monstername'])

        if monster:
            return monster.json(), 200
        return {'message': 'Monster not found.'}, 404

    @jwt_required
    def put(self):
        data = Monster.parser.parse_args()
        monster = MonsterModel.find_by_levelname_and_monstername(data['levelname'], data['old_monstername'])      
        if monster is None:
            if MonsterModel.find_by_levelname_and_monstername(data['levelname'], data['monstername']):
                return {'message': "A monster with name '{}' already exists in level '{}'.".format(data['monstername'], data['levelname'])}, 404
            else:
                monster = MonsterModel(data['monstername'], data['atk'], data['hp'], data['max_hp'], data['sprite'], data['levelname'])
                monster.save_to_db()
                return {'message': "Monster '{}' created successfully.".format(data['monstername'])}, 201
        else:
            if MonsterModel.find_by_levelname_and_monstername(data['levelname'], data['monstername']):
                return {'message': "A monster with name '{}' already exists in level '{}'.".format(data['monstername'], data['levelname'])}, 404
            else:
                monster.monstername = data['monstername']
                monster.atk = data['atk']
                monster.hp = data['hp']
                monster.max_hp = data['max_hp']
                monster.sprite = data['sprite']
                monster.levelname = data['levelname']              
                monster.save_to_db()
                return {'message': "Monster updated."}, 200

    @fresh_jwt_required
    def delete(self):
        data = Monster.parser.parse_args()

        monster = MonsterModel.find_by_levelname_and_monstername(data['levelname'], data['monstername'])

        if monster:
            monster.delete_from_db()
            return{"message": "Monster deleted."}, 200
        else:
            return{"message": "That monster does not exist."}, 404