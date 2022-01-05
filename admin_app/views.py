
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from flask_admin.model.helpers import get_mdict_item_or_list
from flask import abort, session, request
from werkzeug.utils import redirect
from admin_app.forms import ProjectForm
from admin_app.models import ProjectModel


class ProjectModelView(ModelView):
    # Customizing default templates
    # create_template = 'admin/create-project.html'
    # edit_template = 'admin/edit-project.html'
    
    # accessability
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            return redirect('/login')

    form = ProjectForm

class HomeView(AdminIndexView):
    @expose('/')
    def index(self):
        # id = get_mdict_item_or_list(request.args, 'id')
        # model = self.get_one(id)
        projects = ProjectModel.query.all()
        return self.render('admin/index.html', projects=projects)