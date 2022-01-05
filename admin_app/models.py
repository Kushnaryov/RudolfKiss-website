from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class ProjectModel(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key = True)
    order_num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    video_url = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(30))
    