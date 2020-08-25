import sqlite3
from db import db


class LevelModel(db.Model):
    __tablename__ = "levels"

    id = db.Column(db.Integer, primary_key=True)
    levelname = db.Column(db.String(50), unique=True)

    monster1name = db.Column(db.String(50))
    monster1atk = db.Column(db.Integer)
    monster1hp = db.Column(db.Integer)    
    monster1max_hp = db.Column(db.Integer)  
    monster1sprite = db.Column(db.String)

    monster2name = db.Column(db.String(50))
    monster2atk = db.Column(db.Integer)
    monster2hp = db.Column(db.Integer)    
    monster2max_hp = db.Column(db.Integer)  
    monster2sprite = db.Column(db.String)

    monster3name = db.Column(db.String(50))
    monster3atk = db.Column(db.Integer)
    monster3hp = db.Column(db.Integer)    
    monster3max_hp = db.Column(db.Integer)  
    monster3sprite = db.Column(db.String)

    monster4name = db.Column(db.String(50))
    monster4atk = db.Column(db.Integer)
    monster4hp = db.Column(db.Integer)    
    monster4max_hp = db.Column(db.Integer)  
    monster4sprite = db.Column(db.String)  

    def __init__(self, levelname, monster1name, monster1atk, monster1hp, monster1max_hp, monster1sprite, monster2name, monster2atk, monster2hp, monster2max_hp, monster2sprite, monster3name, monster3atk, monster3hp, monster3max_hp, monster3sprite, monster4name, monster4atk, monster4hp, monster4max_hp, monster4sprite):
        self.levelname = levelname
        self.monster1name = monster1name
        self.monster1atk = monster1atk
        self.monster1hp = monster1hp
        self.monster1max_hp = monster1max_hp
        self.monster1sprite = monster1sprite
        self.monster2name = monster2name
        self.monster2atk = monster2atk
        self.monster2hp = monster2hp
        self.monster2max_hp = monster2max_hp
        self.monster2sprite = monster2sprite
        self.monster3name = monster3name
        self.monster3atk = monster3atk
        self.monster3hp = monster3hp
        self.monster3max_hp = monster3max_hp
        self.monster3sprite = monster3sprite
        self.monster4name = monster4name
        self.monster4atk = monster4atk
        self.monster4hp = monster4hp
        self.monster4max_hp = monster4max_hp
        self.monster4sprite = monster4sprite

    def json(self):
        return {
            'levelname': self.levelname, 
            'monster1name': self.monster1name, 
            'monster1atk': self.monster1atk, 
            'monster1hp': self.monster1hp, 
            'monster1max_hp': self.monster1max_hp, 
            'monster1sprite': self.monster1sprite,
            'monster2name': self.monster2name, 
            'monster2atk': self.monster2atk, 
            'monster2hp': self.monster2hp, 
            'monster2max_hp': self.monster2max_hp, 
            'monster2sprite': self.monster2sprite,
            'monster3name': self.monster3name, 
            'monster3atk': self.monster3atk, 
            'monster3hp': self.monster3hp, 
            'monster3max_hp': self.monster3max_hp, 
            'monster3sprite': self.monster3sprite,
            'monster4name': self.monster4name, 
            'monster4atk': self.monster4atk, 
            'monster4hp': self.monster4hp, 
            'monster4max_hp': self.monster4max_hp, 
            'monster4sprite': self.monster4sprite
            }

    @classmethod
    def find_by_levelname(cls, levelname):
        level = cls.query.filter_by(levelname=levelname).first()
        return level