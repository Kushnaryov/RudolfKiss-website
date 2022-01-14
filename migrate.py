from app import db, app
from main_app.models import User
# from flask_migrate import Migrate

# migrate = Migrate()

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add(User(username='admin', password='admin'))
    db.session.commit()



