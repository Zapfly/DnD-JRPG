from db import db

class UserModel(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(80))
    

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'user_id': self.id, 'username': self.username, 'password': self.password}
    
    @classmethod
    def find_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        return user

    @classmethod
    def find_by_username_and_password(cls, username, password):
        user = cls.query.filter_by(username=username, password=password).first()
        return user   

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()    
      
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()