from flask import session, redirect, request, render_template

# @app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# @app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == "Adam" and request.form.get('password') == '12345':
            session['logged_in'] = True
            return redirect('/admin')
        else:
            return render_template('auth/login.html', failed=True) 
    return render_template('auth/login.html') 