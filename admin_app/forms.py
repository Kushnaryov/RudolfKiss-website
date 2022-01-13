from wtforms.form import Form
from wtforms.fields import SelectField
from wtforms.fields.simple import StringField
from wtforms.validators import ValidationError, InputRequired
from admin_app.UploadField import FileUploadField
import main_app.settings as settings

allowed_ext = {'mp4'}

def IntegerValidator(form, field):
    try:
        int(field.data)
    except:
        raise ValidationError('Field must an integer')


class ProjectForm(Form):
    order_num = StringField('Order number', validators=[InputRequired(), IntegerValidator])
    # name = StringField('Name', validators=[InputRequired()])
    video_url = StringField('video_url', validators=[InputRequired()])
    # video_url = FileUploadField(
    #                             'Video', 
    #                             base_path=settings.content_path, 
    #                             allowed_extensions = allowed_ext,
    #                             validators=[InputRequired()])
    category = SelectField(u'category', choices=[('NEW STUFF', 'NEW STUFF'),
                                                 ('COMMERCIALS', 'COMMERCIALS'), 
                                                 ('CINEMATOGRAPHY WORK', 'CINEMATOGRAPHY WORK'),
                                                 ('MUSIC VIDEOS', 'MUSIC VIDEOS'),
                                                 ('DOCUMENTARIES', 'DOCUMENTARIES'), 
                                                 ('SHORT FILMS', 'SHORT FILMS'),
                                                 ('SHOWREEL', 'SHOWREEL'),
                                                 ('background', 'BACKGROUND')])
    # slug = StringField('Slug', validators=[InputRequired()])
