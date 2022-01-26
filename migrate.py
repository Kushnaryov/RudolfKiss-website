from app import db, app
from main_app.models import User
# from flask_migrate import Migrate

# migrate = Migrate()

NEW_STUFF = [
    'https://vimeo.com/414703865',
    'https://vimeo.com/662897822',
    'https://vimeo.com/260382981',
    'https://vimeo.com/205722901',
    'https://vimeo.com/460274301',
    'https://vimeo.com/248956245',
    'https://vimeo.com/248876338',
    'https://vimeo.com/212655943',
    'https://vimeo.com/414881973',
    'https://vimeo.com/414706013',
    'https://vimeo.com/414705968',
    'https://vimeo.com/342659882',
    'https://vimeo.com/661708694',
    'https://vimeo.com/414703472',
    'https://vimeo.com/414704957',
    'https://vimeo.com/340081349',
    'https://vimeo.com/212655912',
    'https://vimeo.com/260557341',
    'https://vimeo.com/212656474',
    'https://vimeo.com/662898917',
    'https://vimeo.com/302720529',
    'https://vimeo.com/212656415',
    'https://vimeo.com/248907525',
    'https://vimeo.com/260382394',
    'https://vimeo.com/260553314'
]

COMMERCIALS = [
    'https://vimeo.com/212655759',
    'https://vimeo.com/414884576',
    'https://vimeo.com/414883786',
    'https://vimeo.com/260339106',
    'https://vimeo.com/212656346',
    'https://vimeo.com/212656254',
    'https://vimeo.com/305467027',
    'https://vimeo.com/302778933',
    'https://vimeo.com/260382037',
    'https://vimeo.com/111517864',
    'https://vimeo.com/212656958',
    'https://vimeo.com/305466973',
    'https://vimeo.com/67499655',
    'https://vimeo.com/57006455',
    'https://vimeo.com/56990646',
]

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add(User(username='admin', password='admin'))
    db.session.commit()



