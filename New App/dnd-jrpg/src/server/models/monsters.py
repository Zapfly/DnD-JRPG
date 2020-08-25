import sqlite3
from db import db


class MonsterModel(db.Model):
    __tablename__ = "monsters"

    id = db.Column(db.Integer, primary_key=True)
    monstername = db.Column(db.String(50))
    atk = db.Column(db.Integer)
    hp = db.Column(db.Integer)    
    max_hp = db.Column(db.Integer)  
    sprite = db.Column(db.String)
    levelname = db.Column(db.String, db.ForeignKey('levels.levelname'))
    level = db.relationship('LevelModel')    

    def __init__(self, monstername, atk, hp, max_hp, sprite, levelname):
        self.monstername = monstername
        self.atk = atk
        self.hp = hp
        self.max_hp = max_hp
        self.sprite = sprite
        self.levelname = levelname

    def json(self):
        return {'monstername': self.monstername, 'atk': self.atk, 'hp': self.hp, 'max_hp': self.max_hp, 'sprite': self.sprite, 'levelname': self.levelname}

    @classmethod
    def find_by_levelname(cls, levelname):
        return cls.query.filter_by(levelname=levelname).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        connection = sqlite3.connect('data.db')
        db.session.delete(self)
        db.session.commit()