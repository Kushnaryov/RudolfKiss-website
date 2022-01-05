from flask import abort, render_template, send_from_directory
from sqlalchemy.orm.exc import NoResultFound

from admin_app.models import ProjectModel

def home():
    try:   
        projects = ProjectModel.query.all()
        background = ProjectModel.query.filter(category='background')
        return render_template("index.html", projects=projects, background=background)
    except NoResultFound:
        abort(404) 

# def content(path):
#     return send_from_directory("content", path)