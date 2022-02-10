from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class NewStuff(db.Model):
    __tablename__ = 'NewStuff'
    id = db.Column(db.Integer, primary_key = True)
    order_num = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    start = db.Column(db.Integer)
    length = db.Column(db.Integer)
    category = db.Column(db.String(10), 
                        nullable=False, 
                        default='Background')
    encoded_name = db.Column(db.String(100))
    video_url = db.Column(db.String(50), nullable=False)
    video_embed = db.Column(db.String(150))
    bucket_url = db.Column(db.String(200))


class Commercials(db.Model):
    __tablename__ = 'Commercials'
    id = db.Column(db.Integer, primary_key = True)
    order_num = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    start = db.Column(db.Integer)
    length = db.Column(db.Integer)
    category = db.Column(db.String(10), 
                        nullable=False, 
                        default='Background')
    encoded_name = db.Column(db.String(100))
    video_url = db.Column(db.String(50), nullable=False)
    video_embed = db.Column(db.String(150))
    bucket_url = db.Column(db.String(200))

class MusicVideos(db.Model):
    __tablename__ = 'MusicVideos'
    id = db.Column(db.Integer, primary_key = True)
    order_num = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    start = db.Column(db.Integer)
    length = db.Column(db.Integer)
    category = db.Column(db.String(10), 
                        nullable=False, 
                        default='Background')
    encoded_name = db.Column(db.String(100))
    video_url = db.Column(db.String(50), nullable=False)
    video_embed = db.Column(db.String(150))
    bucket_url = db.Column(db.String(200))

class ShortFilms(db.Model):
    __tablename__ = 'ShortFilms'
    id = db.Column(db.Integer, primary_key = True)
    order_num = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    start = db.Column(db.Integer)
    length = db.Column(db.Integer)
    category = db.Column(db.String(10), 
                        nullable=False, 
                        default='Background')
    encoded_name = db.Column(db.String(100))
    video_url = db.Column(db.String(50), nullable=False)
    video_embed = db.Column(db.String(150))
    bucket_url = db.Column(db.String(200))

class Documentaries(db.Model):
    __tablename__ = 'Documentaries'
    id = db.Column(db.Integer, primary_key = True)
    order_num = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    start = db.Column(db.Integer)
    length = db.Column(db.Integer)
    category = db.Column(db.String(10), 
                        nullable=False, 
                        default='Background')
    encoded_name = db.Column(db.String(100))
    video_url = db.Column(db.String(50), nullable=False)
    video_embed = db.Column(db.String(150))
    bucket_url = db.Column(db.String(200))

class DopWorks(db.Model):
    __tablename__ = 'DopWorks'
    id = db.Column(db.Integer, primary_key = True)
    order_num = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    start = db.Column(db.Integer)
    length = db.Column(db.Integer)
    category = db.Column(db.String(10), 
                        nullable=False, 
                        default='Background')
    encoded_name = db.Column(db.String(100))
    video_url = db.Column(db.String(50), nullable=False)
    video_embed = db.Column(db.String(150))
    bucket_url = db.Column(db.String(200))

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))