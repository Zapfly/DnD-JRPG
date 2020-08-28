from db import db


class LevelModel(db.Model):
    __tablename__ = "levels"

    id = db.Column(db.Integer, primary_key=True)
    levelname = db.Column(db.String(50), unique=True)

    monsters = db.relationship('MonsterModel', lazy='dynamic')

    def __init__(self, levelname):
        self.levelname = levelname

    def json(self):
        return {'levelname': self.levelname, 'monsters': [monster.json() for monster in self.monsters.all()]}

    @classmethod
    def find_by_levelname(cls, levelname):
        level = cls.query.filter_by(levelname=levelname).first()
        return level
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()