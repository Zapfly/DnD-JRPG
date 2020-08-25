import sqlite3
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
    parser.add_argument('monster1name',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster1atk',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster1hp',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster1max_hp',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster1sprite',
        type=str,
        help="A user id is required"
    )
    parser.add_argument('monster2name',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster2atk',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster2hp',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster2max_hp',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster2sprite',
        type=str,
        help="A user id is required"
    )
    parser.add_argument('monster3name',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster3atk',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster3hp',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster3max_hp',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster3sprite',
        type=str,
        help="A user id is required"
    )
    parser.add_argument('monster4name',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster4atk',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster4hp',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster4max_hp',
        type=float,
        help="This field cannot be left blank!"
    )
    parser.add_argument('monster4sprite',
        type=str,
        help="A user id is required"
    )

    def get(self):
        data = Level.parcer.parse_args()

        level = LevelModel.find_by_levelname(data['levelname'])

        if level:
            return level.json(), 200
        return {'message': 'A level with that name does not exist'}, 404
        