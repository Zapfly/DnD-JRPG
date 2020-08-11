import sqlite3
from db import db


class HeroModel(db.Model):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    heroname = db.Column(db.String(50))
    atk = db.Column(db.Integer)
    hp = db.Column(db.Integer)    
    max_hp = db.Column(db.Integer)  
    sprite = db.Column(db.String)     
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, username, heroname, atk, hp, max_hp, sprite, user_id):
        self.username = username
        self.heroname = heroname
        self.atk = atk
        self.hp = hp
        self.max_hp = max_hp
        self.sprite = sprite
        self.user_id = user_id

    def json(self):
        return {'username': self.username, 'heroname': self.heroname, 'atk': self.atk, 'hp': self.hp, 'max_hp': self.max_hp, 'sprite': self.sprite, 'user_id': self.user_id}


    @classmethod
    def find_by_user_id_and_heroname(cls, user_id, heroname):
        return cls.query.filter_by(user_id=user_id, heroname=heroname).first()
    # def insert(cls, hero):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "INSERT INTO heroes VALUES (NULL, ?, ?, ?, ?, ?, ?)"
    #     cursor.execute(query, (hero['username'], hero['heroname'], hero['atk'], hero['hp'], hero['max_hp'], hero['sprite']))

    #     connection.commit()
    #     connection.close()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        connection = sqlite3.connect('data.db')
        db.session.delete(self)
        db.session.commit()
