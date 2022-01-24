from flask import abort, render_template, request
from sqlalchemy import desc
from sqlalchemy.orm.exc import NoResultFound
from main_app.settings import *
from main_app.models import Works, Backgrounds
from admin_app.helpers import start_s3_client
def home():
    category = "NEW STUFF"
    try:   
        projects = Works.query.order_by(desc(Works.order_num)).filter_by(category=category)
        works = []
        for project in projects:
            if project.encoded_name != None:
                title_1 = project.first_name
                title_2 = project.second_name
                separator = ' / ' #if title_2 != '' else ''
                dic = {
                    'title_1': title_1,
                    'title_2': title_2,
                    'separator': separator,
                    'name': project.encoded_name, # url from bucket 
                    'video_embed': project.video_embed,
                    'bucket_url' : project.bucket_url
                }
                works.append(dic)
        try:
            bucket_url = Backgrounds.query.filter_by(page=category).one().bucket_url
        except:
            bucket_url =f'https://s3.{S3_REGION}.amazonaws.com/{S3_BUCKET}/{content_path}default_background.mp4'

        return render_template("index.html", works=works, background=bucket_url)
    except:
        abort(404)

 




# def content(path):
#     return send_from_directory("content", path)