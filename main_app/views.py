from flask import abort, render_template, request
from sqlalchemy.orm.exc import NoResultFound

from main_app.models import Works

def home():
    category = "NEW STUFF"
    if request.method == 'POST':
        category = request.form['category']
        print(category)
    try:   
        projects = Works.query.filter_by(category=category)
        works = []
        for project in projects:
            if project.name != None:
                title_1, title_2 = project.name.split(' _ ')
                dic = {
                    'title_1': title_1,
                    'title_2': title_2,
                    'name': project.name,
                    'video_embed': project.video_embed
                }
                works.append(dic)
        # test_text = projects[0].video_url
        bg_url ='/media/content/' + 'background.mp4'#Works.query.filter_by(category='background').one().video_url
        return render_template("index.html", works=works, background=bg_url, category=category) #, test_text=test_text 
    except NoResultFound:
        abort(404)

 




# def content(path):
#     return send_from_directory("content", path)