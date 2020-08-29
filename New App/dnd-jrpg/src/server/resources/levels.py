from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from models.levels import LevelModel


class Level(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('levelname',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('old_levelname',
        type=str,
    )

    @jwt_required()
    def post(self):
        data = Level.parser.parse_args()

        if LevelModel.find_by_levelname(data['levelname']):
            return {'message': "A level with name '{}' already exists.".format(data['levelname'])}, 404
        
        level = LevelModel(data['levelname'])
        try:
            level.save_to_db()
        except:
            return {'message': "An error occurred creating the level."}, 500

        return level.json(), 201

    @jwt_required()
    def get(self):
        data = Level.parser.parse_args()

        level = LevelModel.find_by_levelname(data['levelname'])

        if level:
            return level.json(), 200
        return {'message': 'Level not found'}, 404

    @jwt_required()
    def put(self):
        data = Level.parser.parse_args()
        level = LevelModel.find_by_levelname(data['old_levelname'])      
        if level is None:
            if LevelModel.find_by_levelname(data['levelname']):
                return {'message': "A level with name '{}' already exists.".format(data['levelname'])}, 404
            else:
                level = LevelModel(data['levelname'])
                level.save_to_db()
                return {'message': "Level '{}' created successfully.".format(data['levelname'])}, 201
        else:
            if LevelModel.find_by_levelname(data['levelname']):
                return {'message': "A level with name '{}' already exists.".format(data['levelname'])}, 404
            else:
                level.levelname = data['levelname']
                level.save_to_db()
                return {'message': 'Level updated successfully.'}, 200

    @jwt_required()
    def delete(self):
        data = Level.parser.parse_args()

        level = LevelModel.find_by_levelname(data['levelname'])

        if level:
            level.delete_from_db()
            return {'message': "Level '{}' deleted.".format(data['levelname'])}, 200
        return {'message': 'That level does not exist.'}, 404


class LevelList(Resource):
    @jwt_required()
    def get(self):
        return {'levels': [level.json() for level in LevelModel.query.all()]}
