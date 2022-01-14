from flask import session, redirect, request, render_template
from main_app.models import User
from flask_login import current_user, login_user, logout_user
from flask_admin.menu import MenuLink
class LoginMenuLink(MenuLink):
    def is_accessible(self):
        return not current_user.is_authenticated 

class LogoutMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated      


# @app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

# @app.route("/login", methods=['GET', 'POST'])
def login():
    name = User.query.one().username
    password = User.query.one().password
    if request.method == 'POST':
        if request.form.get('username') == name and request.form.get('password') == password: # to encrypt this
            login_user(User.query.get(1))
            return redirect('/admin/works')
        else:
            return render_template('auth/login.html', failed=True) 
    return render_template('auth/login.html')
