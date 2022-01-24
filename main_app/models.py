from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Works(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key = True)
    order_num = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    start = db.Column(db.Integer)
    length = db.Column(db.Integer)
    category = db.Column(db.String(20), nullable=False)
    encoded_name = db.Column(db.String(100))
    video_url = db.Column(db.String(50), nullable=False, unique=True)
    video_embed = db.Column(db.String(150))
    bucket_url = db.Column(db.String(200))


class Backgrounds(db.Model):
    __tablename__ = 'Backgrounds'
    id = db.Column(db.Integer, primary_key = True)
    start = db.Column(db.Integer)
    length = db.Column(db.Integer)
    encoded_name = db.Column(db.String(100))
    video_url = db.Column(db.String(50), nullable=False)
    page = db.Column(db.String(20), nullable=False, unique=True)
    bucket_url = db.Column(db.String(200))


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))