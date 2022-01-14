from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from flask_admin.babel import gettext
from flask import session, flash

from werkzeug.utils import redirect
from admin_app.forms import ProjectForm
from admin_app.helpers import get_name, create_gif_png, delete_gif_png, update_gif_png, get_embed_url
from main_app.settings import content_path

class WorksView(ModelView):
    # Customizing default templates
    # create_template = 'admin/create-project.html'
    # edit_template = 'admin/edit-project.html'
    
    # accessability
    def is_accessible(self):
        return current_user.is_authenticated
    def is_inaccessible(self):
        return redirect('/login')

    form = ProjectForm

    def update_model(self, form, model):
        old_name = model.name
        super(WorksView, self).update_model(form, model)
        new_name = get_name(model.video_url)
        if old_name != new_name:
            update_gif_png(model.video_url, content_path, old_name, new_name, 2, 7)
            model.name = new_name
            model.video_embed = get_embed_url(model.video_url)
            self.session.commit()

    def create_model(self, form):
        try:
            model = self.build_new_instance()

            form.populate_obj(model)
            self.session.add(model)
            self._on_model_change(form, model, True)
            # custom functionality
            model.name = get_name(model.video_url)
            model.video_embed = get_embed_url(model.video_url)
            #
            self.session.commit()

            # custom
            create_gif_png(url=model.video_url, path=content_path, filename=model.name, start=2, end=7)

        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to create record. %(error)s', error=str(ex)), 'error')
                # log.exception('Failed to create record.')

            self.session.rollback()

            return False
        else:
            self.after_model_change(form, model, True)

        return model


    def delete_model(self, model):
        name = model.name
        super(WorksView, self).delete_model(model)
        delete_gif_png(content_path, name)

class HomeView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    def is_inaccessible(self):
        return redirect('/login')

    def is_visible(self):
        # This view won't appear in the menu structure
        return False

    @expose('/')
    def index(self):
        return redirect('/admin/works')

class UserView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def is_inaccessible(self):
        return redirect('/login')

    can_create = False
    can_delete = False


    

