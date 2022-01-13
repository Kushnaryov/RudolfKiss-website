from app import db, app
# from flask_migrate import Migrate

# migrate = Migrate()

with app.app_context():
    db.drop_all()
    db.create_all()
