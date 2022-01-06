import os
from secrets import token_urlsafe

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = token_urlsafe(16)
# DATABASE_FILE = 'dd7fn5k9enmm1m'

content_dir_name = 'static/media/content'
app_dir = os.path.realpath(os.path.dirname(__file__))
content_path = os.path.join(app_dir, content_dir_name)
# db_path = os.path.join(app_dir, DATABASE_FILE)

DEV_DB_URI = 'postgresql://postgres:joydivision32@localhost/RudolfKiss'
PROD_DB_URI = 'postgres://sodluwekofgiyz:4bcb5a2885a5b3613a650bac01ab565d5c33ede79120649ef2bc3dc0e7548e58@ec2-54-220-223-3.eu-west-1.compute.amazonaws.com:5432/dd7fn5k9enmm1m'