
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from flask_admin.babel import gettext
from flask import session, flash

from werkzeug.utils import redirect
from admin_app.forms import ProjectForm
from admin_app.models import ProjectModel, fullfill_video_data
from admin_app.helpers import get_name, create_gif_png, delete_gif_png, update_gif_png, get_embed_url
from main_app.settings import content_path

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

    def update_model(self, form, model):
        old_name = model.name
        super(ProjectModelView, self).update_model(form, model)
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
        super(ProjectModelView, self).delete_model(model)
        delete_gif_png(content_path, name)

class HomeView(AdminIndexView):
    @expose('/')
    def index(self):
        # id = get_mdict_item_or_list(request.args, 'id')
        # model = self.get_one(id)
        projects = ProjectModel.query.all()
        works = []
        for project in projects:
            if project.name != None:
                # v = Vimeo(project.video_url)
                # metadata = v.metadata
                # stream_240 = v.streams[0]
                dic = {
                    'name': project.name,
                    # 'video_url': stream_240.direct_url
                }
                works.append(dic)
        return self.render('admin/index.html', works=works)



class rGraphsView(ModelView):
    form_columns = ['graph_id', 'Description', 'TABLE_SRC','G_QUERY']

    def allow_update(self, form, model):
        # test your form data and/or existing model data here
        print (form.G_QUERY.data)
        print (model.G_QUERY)
        # return True or False 
        return True

    # def allow_create(self, form):
    #     # test your form data here
    #     print (form.G_QUERY.data)
    #     # return True or False 
    #     return True

    # def allow_delete(self, model):
    #     # test your model data here
    #     print (model.G_QUERY)
    #     # return True or False 
    #     return True

    def update_model(self, form, model):

        if self.allow_update(form, model):
            # passes our allow_update test call super method
            print ('function when update')
            return super(rGraphsView, self).update_model(form, model)
        else:
            flash('Your failed update message here', 'error')

    def create_model(self, form):

        if self.allow_create(form):
            # passes our allow_create test call super method
            print ('function when create')
            return super(rGraphsView, self).create_model(form)
        else:
            flash('Your failed create message here', 'error')

    def delete_model(self, model):

        if self.allow_delete(model):
            # passes our allow_delete test call super method
            print ('function when delete')
            return super(rGraphsView, self).delete_model(model)
        else:
            flash('Your failed delete message here', 'error')