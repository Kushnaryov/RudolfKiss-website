from flask import abort, render_template, send_from_directory, request
from sqlalchemy.orm.exc import NoResultFound

from admin_app.models import ProjectModel

def home():
    try:   
        projects = ProjectModel.query.filter_by(category='NEW STUFF')
        test_text = request
        bg_url ='/media/content/' + 'background.mp4'#ProjectModel.query.filter_by(category='background').one().video_url
        return render_template("index.html", projects=projects, background=bg_url, test_text=test_text)
    except NoResultFound:
        abort(404) 

# def content(path):
#     return send_from_directory("content", path)