from unicodedata import category
from flask import abort, render_template, request
from sqlalchemy import desc
from main_app.settings import *
from main_app.models import NewStuff, Commercials, MusicVideos, ShortFilms, Documentaries, DopWorks


def home():
    try:   
        projects = NewStuff.query.order_by(desc(NewStuff.order_num)).filter_by(category='Works')
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
                    'bucket_url' : project.bucket_url
                }
                works.append(dic)
        try:
            bg = NewStuff.query.filter_by(category='Background').one()
            separator = ' / ' #if bg.second_name != '' else ''
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
        return render_template("home.html", works=works, background=background)
    except:
        abort(404)

def commercials():
    try:   
        projects = Commercials.query.order_by(desc(Commercials.order_num)).filter_by(category='Works')
        works = []
        for project in projects:
            if project.encoded_name != None:
                separator = ' / ' if project.second_name != '' else ''
                dic = {
                    'title_1': project.first_name,
                    'title_2': project.second_name,
                    'separator': separator,
                    'video_embed': project.video_embed,
                    'video' : project.bucket_url
                }
                works.append(dic)
        print(works)
        try:
            bg = Commercials.query.filter_by(category='Background').one()
            separator = ' / ' #if bg.second_name != '' else ''
            background = {
                'video': bg.bucket_url,
                'title_1': bg.first_name,
                'title_2': bg.second_name,
                'separator': separator
            }
        except:
            print('exited from bg')
            background = { 
                'video' : f'https://s3.{S3_REGION}.amazonaws.com/{S3_BUCKET}/{content_path}default_background.mp4',
                'title_1': 'default background name',
                'title_2': 'default background name',
                'separator': '/'
            }

        return render_template("commercials.html", works=works, background=background)
    except:
        abort(404)

def music_videos():
    projects = MusicVideos.query.order_by(desc(MusicVideos.order_num)).filter_by(category='Works')
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
                'video' : project.bucket_url
            }
            works.append(dic)
    try:
        bg = MusicVideos.query.filter_by(category='Background').one()
        separator = ' / ' #if bg.second_name != '' else ''
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

    return render_template("music-videos.html", works=works, background=background)
 
def short_films():
    works = []
    try:
        projects = ShortFilms.query.order_by(desc(ShortFilms.order_num)).filter_by(category='Background')
        
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
    return render_template("short-films.html", works=works)


def documentaries():
    try:   
        projects = Commercials.query.order_by(desc(Commercials.order_num)).filter_by(category='Works')
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
                    'video' : project.bucket_url
                }
                works.append(dic)
        try:
            bucket_url = Commercials.query.filter_by(category='Background').one().bucket_url
        except:
            bucket_url =f'https://s3.{S3_REGION}.amazonaws.com/{S3_BUCKET}/{content_path}default_background.mp4'

        return render_template("documentaries.html", works=works, background=bucket_url)
    except:
        abort(404)

def dop_works():
    try:   
        projects = Commercials.query.order_by(desc(Commercials.order_num)).filter_by(category='Works')
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
                    'video' : project.bucket_url
                }
                works.append(dic)
        try:
            bucket_url = Commercials.query.filter_by(category='Background').one().bucket_url
        except:
            bucket_url =f'https://s3.{S3_REGION}.amazonaws.com/{S3_BUCKET}/{content_path}default_background.mp4'

        return render_template("dop-works.html", works=works, background=bucket_url)
    except:
        abort(404)


# def content(path):
#     return send_from_directory("content", path)