from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
# from migrate import create_base_user
# from flask_admin.contrib.sqla import ModelView
# from main_app.migrate import migrate

import main_app.views as views
from auth_app import views as auth_views
from main_app.models import Works, db, User
from admin_app.views import WorksView, HomeView, UserView
import main_app.settings as settings

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SECRET_KEY'] = settings.SECRET_KEY

ENV = 'heroku'
# ENV = 'local'

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
        ('/', 'home', views.home, ['GET', 'POST']),
        ('/category=new-stuff', 'new-stuff', views.home),
        ('/login', 'login', auth_views.login, ['GET', 'POST']),
        ('/logout', 'logout', auth_views.logout)
                    ]

register_views(views_to_register)

login = LoginManager(app)
admin = Admin(app, template_mode='bootstrap4', index_view=HomeView())

admin.add_view(WorksView(Works, db.session))
admin.add_view(UserView(User, db.session))

admin.add_link(auth_views.LogoutMenuLink(name='Logout', category='', url="/logout"))
admin.add_link(auth_views.LoginMenuLink(name='Login', category='', url="/login"))


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == "__main__":
    app.run(use_reloader = True)
