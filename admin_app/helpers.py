import re
import os
from moviepy.editor import VideoFileClip
from vimeo_downloader import Vimeo
from flask import flash


def prepare_name(string: str):
    string = clear_string_from_parentheses(string)
    string = string.replace('/', '_')
    string = string.replace(':', '_')
    splitters = ['_']
    for splitter in splitters:
        if splitter in string:
            first_name = string.split(splitter)[0]
            second_name = clear_string_from_second_divider(string.split(splitter)[1])
            name = f'{first_name}{splitter}{second_name}'
        else:
            name = string
    return name

def clear_string_from_parentheses(string: str):
    return re.sub("( \(.*?\))", "", string)

def clear_string_from_second_divider(string: str):
    return re.sub("( \/.*)", "", string)

def download_video(url: str, path: str):
    v = Vimeo(url)
    name = get_name(url)
    try:
        v.streams[0].download(download_directory=path, filename=name)
    except:
        flash("Cannot connect to the vimeo", category='error')

def create_gif_png(url: str, path: str, filename: str, start: int, end: int):
    download_video(url, path)
    clip = VideoFileClip(f'{path}{filename}.mp4').subclip(start, end)
    clip.save_frame(f'{path}{filename}.png', t = 2)
    clip.write_gif(f'{path}{filename}.gif')
    os.remove(f'{path}{filename}.mp4')

def get_name(url: str):
    try:
        return prepare_name(Vimeo(url).metadata.title)
    except:
        raise ValueError('Video is not on the vimeo')

def get_embed_url(url: str):
    return 'https://player.vimeo.com/video/'+url[-9:]

def delete_gif_png(path: str, filename: str):
    try:
        os.remove(f'{path}{filename}.png')
        os.remove(f'{path}{filename}.gif')
    except:
        pass

def update_gif_png(url: str, path: str, old_filename: str, new_filename: str, start: int, end: int):
    delete_gif_png(path, old_filename)
    create_gif_png(url, path, new_filename, start, end)