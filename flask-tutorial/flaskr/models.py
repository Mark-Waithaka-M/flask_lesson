from . import db as db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable= False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), )
    posts = db.relationship('Post.author_id')
    
    def __init__(self, id, name, password):
        self.email=email
        self.name= name
        self.password= password
        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.String(50), nullable=False, default=str(datetime.now()).split(".")[0])
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.ForeignKey('user.id'), default=None)
     
     
    def __init__(self, created, title, body):
        self.created = created
        self.title = title
        self.body = body