from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from main_app.settings import content_path
import os

from admin_app.helpers import get_name, get_embed_url, create_gif_png

db = SQLAlchemy()

class ProjectModel(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key = True)
    order_num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100))
    video_url = db.Column(db.String(50), nullable=False, unique=True)
    category = db.Column(db.String(20), nullable=False)
    video_embed = db.Column(db.String(100))



def process_videos():
    projects = ProjectModel.query.filter_by(category='NEW STUFF')
    for project in projects:
        if project.name == None:
                
                name = get_name(project.video_url)
                embed = get_embed_url(project.video_url)
                create_gif_png(url=project.video_url, path=content_path, filename=name, start=2, end=7)
                project.name = name
                project.video_embed = embed
                db.session.commit()
                
        else:
            try:
                with open(f'{content_path}{project.name}.gif', 'r') as gif:
                    gif.close()
                print (project.name)
            except:
                name = get_name(project.video_url)
                embed = get_embed_url(project.video_url)
                create_gif_png(url=project.video_url, path=content_path, filename=name, start=2, end=7)
                project.name = name
                project.video_embed = embed
                db.session.commit()

    return redirect('/admin')