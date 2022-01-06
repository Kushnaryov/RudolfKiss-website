from flask import Flask
from flask_admin import Admin

import views
from auth_app import views as auth_views

from admin_app.models import ProjectModel, db
from admin_app.views import ProjectModelView, HomeView
import settings

import os

app = Flask(__name__)

# app.config['DATABASE_FILE'] = settings.DATABASE_FILE
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{settings.DATABASE_FILE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SECRET_KEY'] = settings.SECRET_KEY

ENV = 'heroku'

if ENV == 'local':
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DEV_DB_URI
    app.debug = True
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.PROD_DB_URI
    app.debug = False

db.init_app(app)

def register_views(views_to_register):
    for view in views_to_register:
        if len(view) == 3:
            url, endpoint, function = view
            app.add_url_rule(url, endpoint=endpoint, view_func=function)
        elif len(view) == 4:
            url, endpoint, function, methods = view
            app.add_url_rule(url, endpoint=endpoint, view_func=function, methods=methods)
        

views_to_register = [
        ('/', 'home', views.home),
        ('/login', 'login', auth_views.login, ['GET', 'POST']),
        ('/logout', 'logout', auth_views.logout)
                    ]

register_views(views_to_register)

admin = Admin(app, template_mode='bootstrap4', index_view=HomeView())
admin.add_view(ProjectModelView(ProjectModel, db.session))



if __name__ == "__main__":
    # if not os.path.exists(settings.db_path):
    #     with app.app_context():
    #         db.drop_all()
    #         db.create_all()
    app.run(use_reloader = True)