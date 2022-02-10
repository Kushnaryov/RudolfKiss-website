import os
from dotenv import load_dotenv
from secrets import token_urlsafe

load_dotenv()

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = token_urlsafe(16)
# DATABASE_FILE = 'dd7fn5k9enmm1m'

content_path = 'static/media/'
app_dir = os.path.realpath(os.path.dirname(__file__))
# db_path = os.path.join(app_dir, DATABASE_FILE)

DEV_DB_URI = 'postgresql://postgres:joydivision32@localhost/RudolfKiss'
PROD_DB_URI = os.getenv('HEROKU_PROD_DB_URI')

S3_BUCKET = 'rudolfkiss.com'
S3_REGION = 'eu-central-1'
S3_KEY = os.getenv('AWS_ACCES_KEY')
S3_SECRET = os.getenv('AWS_ACCES_SECRET')

