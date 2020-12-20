from app.db import db, BaseModelMixin

class User(db.Model, BaseModelMixin):
    __tablename__ = 'user'

    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String)
    image_url = db.Column('image_url', db.String)
    type = db.Column('type', db.String)
    link = db.Column('link', db.String)

    def __init__(self, id, username, image_url, type, link):
        self.id = id
        self.username = username
        self.image_url = image_url
        self.type = type
        self.link = link

    def __repr__(self):
        return 'User({self.username, self.id, self.image_url, self.type, self.link})'

    def __str__(self):
        return self.username
