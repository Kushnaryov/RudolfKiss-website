from flask import abort, render_template, request
from sqlalchemy.orm.exc import NoResultFound
from vimeo_downloader import Vimeo

from admin_app.models import ProjectModel

def home():
    try:   
        projects = ProjectModel.query.filter_by(category='NEW STUFF')
        works = []
        for project in projects:
            v = Vimeo(project.video_url)
            metadata = v.metadata
            stream_240 = v.streams[0]
            dic = {
                'title': metadata.title,
                'video_url': stream_240.direct_url
            }
            works.append(dic)
        test_text = projects[0].video_url
        bg_url ='/media/content/' + 'background.mp4'#ProjectModel.query.filter_by(category='background').one().video_url
        return render_template("index.html", works=works, background=bg_url, test_text=test_text)
    except NoResultFound:
        abort(404) 


# def content(path):
#     return send_from_directory("content", path)