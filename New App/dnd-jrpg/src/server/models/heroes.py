import sqlite3
from db import db


class HeroModel(db.Model):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    heroname = db.Column(db.String(50))
    atk = db.Column(db.Integer)
    hp = db.Column(db.Integer)    
    max_hp = db.Column(db.Integer)  
    sprite = db.Column(db.String)     
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, heroname, atk, hp, max_hp, sprite, user_id):
        self.heroname = heroname
        self.atk = atk
        self.hp = hp
        self.max_hp = max_hp
        self.sprite = sprite
        self.user_id = user_id

    def json(self):
        return {'heroname': self.heroname, 'atk': self.atk, 'hp': self.hp, 'max_hp': self.max_hp, 'sprite': self.sprite, 'user_id': self.user_id}


    @classmethod
    def find_by_user_id_and_heroname(cls, user_id, heroname):
        return cls.query.filter_by(user_id=user_id, heroname=heroname).first()

    @classmethod
    def find_all_by_user_id(cls, user_id):
        hero_list = cls.query.filter_by(user_id=user_id)
        return hero_list
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        connection = sqlite3.connect('data.db')
        db.session.delete(self)
        db.session.commit()
