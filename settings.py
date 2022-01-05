import os
from secrets import token_urlsafe

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = token_urlsafe(16)
DATABASE_FILE = 'dd7fn5k9enmm1m'

content_dir_name = 'static/media/content'

app_dir = os.path.realpath(os.path.dirname(__file__))
content_path = os.path.join(app_dir, content_dir_name)
db_path = os.path.join(app_dir, DATABASE_FILE)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')