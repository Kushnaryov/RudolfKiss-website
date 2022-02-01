from unicodedata import category
from flask import abort, render_template, request
from sqlalchemy import desc
from main_app.settings import *
from main_app.models import NewStuff, Commercials, MusicVideos, ShortFilms, Documentaries, DopWorks

def one_background_and_works(db, template):
    try:   
        projects = db.query.order_by(desc(db.order_num)).filter_by(category='Works')
        works = []
        for project in projects:
            if project.encoded_name != None:
                title_1 = project.first_name
                title_2 = project.second_name
                separator = ' / '
                dic = {
                    'title_1': title_1,
                    'title_2': title_2,
                    'separator': separator,
                    'name': project.encoded_name,
                    'video_embed': project.video_embed,
                    'video' : project.bucket_url
                }
                works.append(dic)
        try:
            bg = db.query.filter_by(category='Background').one()
            separator = ' / ' if bg.second_name != '' else ''
            background = {
                'video': bg.bucket_url,
                'title_1': bg.first_name,
                'title_2': bg.second_name,
                'separator': separator
            }
        except:
            background = { 
                'video' : f'https://s3.{S3_REGION}.amazonaws.com/{S3_BUCKET}/{content_path}default_background.mp4',
                'title_1': 'default background name',
                'title_2': 'default background name',
                'separator': '/'
            }
        return render_template(template, works=works, background=background)
    except:
        abort(404)

def all_backgrounds(db, template):
    works = []
    try:
        projects = db.query.order_by(desc(db.order_num)).filter_by(category='Background')
        
        for project in projects:
            if project.encoded_name != None:
                title_1 = project.first_name
                title_2 = project.second_name
                separator = ' / ' if title_2 != '' else ''
                dic = {
                    'title_1': title_1,
                    'title_2': title_2,
                    'separator': separator,
                    'name': project.encoded_name, # url from bucket 
                    'video_embed': project.video_embed,
                    'video' : project.bucket_url
                }
            works.append(dic)
    except:
        dic ={
            'title_1': 'default',
            'title_2': 'default',
            'separator': '/',
            'video_embed': '#',
            'video' : f'https://s3.{S3_REGION}.amazonaws.com/{S3_BUCKET}/{content_path}default_background.mp4',
            }
        works.append(dic)
    print(len(works))
    return render_template(template, works=works)

def home():
    return one_background_and_works(NewStuff, 'home.html')

def commercials():
    return one_background_and_works(Commercials, "commercials.html")

def music_videos():
    return one_background_and_works(MusicVideos, "music-videos.html")
 
def short_films():
    return all_backgrounds(ShortFilms, 'short-films.html')

def documentaries():
    return all_backgrounds(Documentaries, 'documentaries.html')

def dop_works():
    return all_backgrounds(DopWorks, 'dop-works.html')