from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Works(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key = True)
    order_num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100))
    video_url = db.Column(db.String(50), nullable=False, unique=True)
    category = db.Column(db.String(20), nullable=False)
    video_embed = db.Column(db.String(100))

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))