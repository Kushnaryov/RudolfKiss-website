from statistics import mode
from flask.helpers import url_for
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from flask_admin.babel import gettext
from flask import session, flash

from werkzeug.utils import redirect
from admin_app.forms import VideoForm, BackgroundForm
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


class NewStuffView(AccessModelView):
    # variables to override in specific VideoModelViews
    column_list = ['order_num', 'first_name', 'second_name','start', 'length', 'video_url', 'category']
    form = VideoForm
    #

    def create_model(self, form):
        try:
            model = self.build_new_instance()
            form.populate_obj(model)
            self.session.add(model)
            self._on_model_change(form, model, True)

            # custom functionality
            usage = 'small' if model.category == 'Works' else 'background'

            first_name, second_name = get_display_names(model.video_url)
            encoded_name = get_name(model.video_url)
            embed_url = get_embed_url(model.video_url)

            model.first_name = first_name if 'autofill' in model.first_name else model.first_name
            model.second_name = second_name if 'autofill' in model.second_name else model.second_name
            model.encoded_name = encoded_name 
            model.video_embed = embed_url
            
            create_mp4(model.video_url, content_path, encoded_name , usage, model.start, int(model.start)+int(model.length))
            upload_file_to_bucket(content_path, encoded_name, usage)
            model.bucket_url = get_bucket_url(content_path, encoded_name, usage)

            self.session.commit()
            #
            
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to create record. %(error)s', error=str(ex)), 'error')
            self.session.rollback()
            return False
        else:
            self.after_model_change(form, model, True)
        return model

    def update_model(self, form, model):
        old_encoded_name = model.encoded_name
        old_start = model.start
        old_length = model.length
        super(NewStuffView, self).update_model(form, model)
        new_start = model.start
        new_length = model.length
        new_encoded_name = get_name(model.video_url)
        if (old_encoded_name != new_encoded_name) or (old_length != new_length) or (old_start != new_start):
            self.delete_model(model)
            self.create_model(form)
        new_first_name = model.first_name
        new_second_name = model.second_name
        if 'autofill' in new_first_name:
            model.first_name, _ = get_display_names(model.video_url)
        if 'autofill' in new_second_name:
            _, model.second_name = get_display_names(model.video_url)
        self.session.commit()

    def delete_model(self, model):
        usage = 'small' if model.category == 'Works' else 'background'
        encoded_name  = model.encoded_name
        delete_file_from_bucket(content_path, encoded_name, usage)
        super(NewStuffView, self).delete_model(model)
        delete_mp4(content_path, encoded_name, usage)


class CommercialsView(NewStuffView):
    column_list = ['order_num', 'first_name', 'second_name','start', 'length', 'video_url', 'category']

class MusicVideosView(NewStuffView):
    column_list = ['order_num', 'first_name', 'second_name','start', 'length', 'video_url', 'category']

class ShortFilmsView(NewStuffView):
    column_list = ['order_num', 'first_name', 'second_name','start', 'length', 'video_url', 'category']

class DocumentariesView(NewStuffView):
    column_list = ['order_num', 'first_name', 'second_name','start', 'length', 'video_url', 'category']

class DopWorksView(NewStuffView):
    column_list = ['order_num', 'first_name', 'second_name','start', 'length', 'video_url', 'category']
class UserView(AccessModelView):
    can_create = False
    can_delete = False


    

