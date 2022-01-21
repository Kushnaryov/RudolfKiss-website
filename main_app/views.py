from flask import abort, render_template, request
from sqlalchemy.orm.exc import NoResultFound
from main_app.settings import *
from main_app.models import Works, Backgrounds
from admin_app.helpers import start_s3_client
def home():
    category = "NEW STUFF"
    try:   
        projects = Works.query.filter_by(category=category)
        works = []
        for project in projects:
            if project.name != None:
                title_1, title_2 = project.name.replace('_', ' ').split('-')
                dic = {
                    'title_1': title_1,
                    'title_2': title_2,
                    'name': project.name, # url from bucket 
                    'video_embed': project.video_embed,
                    'bucket_url' : project.bucket_url
                }
                works.append(dic)
        # test_text = projects[0].video_url
        try:
            bucket_url = Backgrounds.query.filter_by(page=category).one().bucket_url
        except:
            bucket_url =f'https://s3.{S3_REGION}.amazonaws.com/{S3_BUCKET}/{content_path}default_background.mp4'
        # s3_client = start_s3_client()
        # bg = s3_client.object.get(S3_BUCKET, bg_key)
        # print (bg)
        return render_template("index.html", works=works, background=bucket_url)
    except:
        # raise(FileNotFoundError, 'Background not found')
        abort(404)

 




# def content(path):
#     return send_from_directory("content", path)