from flask.helpers import url_for
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from flask_admin.babel import gettext
from flask import session, flash

from werkzeug.utils import redirect
from admin_app.forms import ProjectForm, BackgroundForm
from admin_app.helpers import *
from main_app.settings import content_path


class HomeView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return redirect('/login')

    def is_visible(self):
        # This view won't appear in the menu structure
        return False

    @expose('/')
    def index(self):
        return redirect('/admin/works')


class AccessModelView(ModelView):
    # Customizing default templates
    create_template = 'admin/create-project.html'
    edit_template = 'admin/edit-project.html'
    list_template = 'admin/list-project.html'

    # accessability
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return redirect('/login')


class VideoModelView(AccessModelView):
    # variables to override in specific VideoModelViews
    usage = ''
    video_start = 0
    video_end = 5
    #

    def create_model(self, form):
        try:
            model = self.build_new_instance()
            form.populate_obj(model)
            self.session.add(model)
            self._on_model_change(form, model, True)

            # custom functionality
            name = get_name(model.video_url)
            embed_url = get_embed_url(model.video_url)
            model.name = name
            model.video_embed = embed_url
            
            create_mp4(model.video_url, content_path, name, self.usage, self.video_start, self.video_end)
            upload_file_to_bucket(content_path, name, self.usage)
            model.bucket_url = get_bucket_url(content_path, name, self.usage)
            self.session.commit()
            #
            
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to create record. %(error)s', error=str(ex)), 'error')
                # log.exception('Failed to create record.')
            self.session.rollback()
            return False
        else:
            self.after_model_change(form, model, True)
        return model

    def update_model(self, form, model):
        old_name = model.name
        super(VideoModelView, self).update_model(form, model)
        new_name = get_name(model.video_url)
        if old_name != new_name:
            update_mp4(model.video_url, content_path, old_name, new_name, self.usage, self.video_start, self.video_end)
            update_file_in_bucket(content_path, old_name, new_name, self.usage)
            model.name = new_name
            model.video_embed = get_embed_url(model.video_url)
            self.session.commit()

    def delete_model(self, model):
        name = model.name
        delete_file_from_bucket(content_path, name, self.usage)
        super(VideoModelView, self).delete_model(model)
        delete_mp4(content_path, name, self.usage)


class WorksView(VideoModelView):
    usage = 'small'
    video_start = 2
    video_end = 7
    
    form = ProjectForm


class BackgroundsView(VideoModelView):
    usage = 'background'
    video_start = 1
    video_end = 21

    form = BackgroundForm


class UserView(AccessModelView):
    can_create = False
    can_delete = False


    

