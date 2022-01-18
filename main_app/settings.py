import os
from secrets import token_urlsafe

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = token_urlsafe(16)
# DATABASE_FILE = 'dd7fn5k9enmm1m'

content_path = 'static/media/videos/'
app_dir = os.path.realpath(os.path.dirname(__file__))
# db_path = os.path.join(app_dir, DATABASE_FILE)

DEV_DB_URI = 'postgresql://postgres:joydivision32@localhost/RudolfKiss'
PROD_DB_URI = 'postgresql://kmwxpdyyexwybk:bfb5b1676e82a15d198ab2f38b8f05314a0fa4defda98f542fe2636b68859aaf@ec2-34-249-49-9.eu-west-1.compute.amazonaws.com:5432/d6vpkslpcd5ad4'