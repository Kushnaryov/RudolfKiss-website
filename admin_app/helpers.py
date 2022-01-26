import re, os
from vimeo_downloader import Vimeo
from main_app.settings import S3_KEY, S3_SECRET, S3_BUCKET, S3_REGION
import boto3
import datetime


def clear_string_from_parentheses(string: str):
    return re.sub("(\(.*?\))", "", string)

def clear_string_from_second_divider(string: str):
    return re.sub("(\/.*)", "", string)

def download_video(url: str, path: str, quality='min'):
    quality = 0 if quality == 'min' else -1
    v = Vimeo(url)
    name = get_name(url)
    try:
        v.streams[quality].download(download_directory=path, filename=name)
    except:
        raise ValueError('Cannot download video from vimeo. Try again, or another')

def create_mp4(url: str, path: str, filename: str, usage: str,  start: int, end: int):
    video_start = str(datetime.timedelta(seconds=int(start)))
    video_end = str(datetime.timedelta(seconds=int(end)))
    
    
    # video_start = f'00:00:{start}'
    # video_end = f'00:00:{end}'
    origin_file = f'{path}{filename}.mp4'
    result_file = f'{path}{filename}_{usage}.mp4'

    if usage == 'small':
        quality = 'min'
        bitrate = '120k'
    elif usage == 'background':
        quality = 'max'
        bitrate = '250k'

    download_video(url, path, quality=quality)
    print('downloaded')
    os.system(f'ffmpeg -ss {video_start} -to {video_end} -i {origin_file} -vcodec libx265 -an -b:v {bitrate} -c:v copy {result_file} -n')
    print('converted to small one')
    os.remove(origin_file)
    print('origin removed')

def remove_all_extra_spaces(string):
    return " ".join(string.split())

def connect_to_vimeo(url: str):
    try:
        return Vimeo(url)    
    except:
        raise ValueError('Cannot get access to the vimeo. Check if url is correct')

def get_display_names(url: str):
    vimeo = Vimeo(url)
    string = vimeo.metadata.title
    string = clear_string_from_parentheses(string)
    string = re.sub("\r?\n|\r/g", "", string)
    
    if ' / ' in string:
        string = string.split(' / ')
        first_name = string[0]
        second_name = clear_string_from_second_divider(string[1])
    elif ': ' in string:
        string = string.split(': ')
        first_name = string[0]
        second_name = clear_string_from_second_divider(string[1])
    else:
        first_name = string
        second_name = ''
    first_name = remove_all_extra_spaces(first_name)
    second_name = remove_all_extra_spaces(second_name)
    return first_name, second_name


def get_name(url: str):
    first_name, second_name = get_display_names(url)
    first_name = re.sub("['!@#$]", '', first_name)
    second_name = re.sub("['!@#$]", '', second_name)
    first_name = first_name.replace(' ', '_')
    second_name = second_name.replace(' ', '_')
    # first_name = first_name.replace('#', '')
    # second_name = second_name.replace('#', '')
    # first_name = first_name.replace('\'', '')
    # second_name = second_name.replace('\'', '')

    splitter = '' if second_name == '' else '-'
    name = f'{first_name}{splitter}{second_name}'
    return name

def get_embed_url(url: str):
    return 'https://player.vimeo.com/video/'+re.findall('\d+|$', url)[0]

def delete_mp4(path: str, filename: str, usage: str):
    try:
        os.remove(f'{path}{filename}_{usage}.mp4')
    except:
        pass

def update_mp4(url: str, path: str, old_filename: str, new_filename: str, usage: str, start: int, end: int):
    delete_mp4(path, old_filename, usage)
    create_mp4(url, path, new_filename, usage, start, end)

def start_s3_client():
    return boto3.client('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)

def upload_file_to_bucket(path: str, filename: str, usage: str):
    file_name = f'{path}{filename}_{usage}.mp4'
    object_name = f'{path}{filename}_{usage}.mp4'
    s3_client = start_s3_client()
    s3_client.upload_file(file_name, S3_BUCKET, object_name)
    print('uploaded')
    os.remove(file_name)
    print('removed from heroku')

def delete_file_from_bucket(path: str, filename: str, usage: str):
    object_name = f'{path}{filename}_{usage}.mp4'
    s3_client = start_s3_client()
    s3_client.delete_object(Bucket=S3_BUCKET, Key=object_name)

def get_bucket_url(path, filename, usage):
    return f'https://s3.{S3_REGION}.amazonaws.com/{S3_BUCKET}/{path}{filename}_{usage}.mp4'

def update_file_in_bucket(path, old_name, new_name, usage):
    delete_file_from_bucket(path, old_name, usage)
    upload_file_to_bucket(path, new_name, usage)

