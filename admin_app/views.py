from statistics import mode
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
            encoded_name = get_name(model.video_url)
            embed_url = get_embed_url(model.video_url)
            model.encoded_name = encoded_name 
            model.video_embed = embed_url
            create_mp4(model.video_url, content_path, encoded_name , self.usage, model.start, int(model.start)+int(model.length))
            upload_file_to_bucket(content_path, encoded_name, self.usage)
            model.bucket_url = get_bucket_url(content_path, encoded_name, self.usage)
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
        super(VideoModelView, self).update_model(form, model)
        new_start = model.start
        new_length = model.length
        new_encoded_name = get_name(model.video_url)
        if (old_encoded_name != new_encoded_name) or (old_length != new_length) or (old_start != new_start):
            self.delete_model(model)
            self.create_model(form)
            # update_mp4(model.video_url, content_path, old_encoded_name, new_encoded_name, self.usage, model.start, int(model.start)+int(model.length))
            # update_file_in_bucket(content_path, old_encoded_name, new_encoded_name, self.usage)
            # model.encoded_name = new_encoded_name
            # model.start = new_start
            # model.length = new_length
            # model.video_embed = get_embed_url(model.video_url)
            # model.bucket_url = get_bucket_url(content_path, model.encoded_name, self.usage)
            # self.session.commit()

    def delete_model(self, model):
        encoded_name  = model.encoded_name
        delete_file_from_bucket(content_path, encoded_name, self.usage)
        super(VideoModelView, self).delete_model(model)
        delete_mp4(content_path, encoded_name, self.usage)


class WorksView(VideoModelView):
    column_list = ['order_num', 'first_name', 'second_name','start', 'length', 'video_url', 'category']
    usage = 'small'
    
    def create_model(self, form):
        model = super().create_model(form)
        first_name, second_name = get_display_names(model.video_url)
        model.first_name = first_name if 'autofill' in model.first_name else model.first_name
        model.second_name = second_name if 'autofill' in model.second_name else model.second_name
        self.session.commit()
        return model
    
    def update_model(self, form, model):
        super().update_model(form, model)
        new_first_name = model.first_name
        print(new_first_name)
        new_second_name = model.second_name
        if 'autofill' in new_first_name:
            model.first_name, _ = get_display_names(model.video_url)
        if 'autofill' in new_second_name:
            _, model.second_name = get_display_names(model.video_url)
        self.session.commit()

    form = ProjectForm


class BackgroundsView(VideoModelView):
    column_list = ['encoded_name', 'start', 'length', 'video_url', 'page']
    usage = 'background'

    form = BackgroundForm


class UserView(AccessModelView):
    can_create = False
    can_delete = False


    

