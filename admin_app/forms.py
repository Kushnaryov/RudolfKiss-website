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


class VideoForm(Form):
    order_num = StringField('Order number', validators=[InputRequired(), IntegerValidator])
    first_name = StringField('First name', default='autofill or type name', validators=[InputRequired()])
    second_name = StringField('Second name', default='autofill or type name', validators=[InputRequired()])
    start = StringField('Start time (sec)', default=2, validators=[InputRequired(), IntegerValidator])
    length = StringField('Sample length (sec)', default=5, validators=[InputRequired(), IntegerValidator])
    video_url = StringField('Video url', validators=[InputRequired()])
    category = SelectField(u'Category', choices=[('Works', 'Works'),
                                                 ('Background', 'Background')])


class BackgroundForm(Form):
    start = StringField('Start time (sec)', default=2, validators=[InputRequired(), IntegerValidator])
    length = StringField('Sample length (sec)', default=20, validators=[InputRequired(), IntegerValidator])
    video_url = StringField('video_url', validators=[InputRequired()])
    page = SelectField(u'page', choices=[('NEW STUFF', 'NEW STUFF'),
                                                 ('COMMERCIALS', 'COMMERCIALS'), 
                                                 ('CINEMA', 'CINEMA'),
                                                 ('MUSIC VIDEOS', 'MUSIC VIDEOS'),
                                                 ('DOCUMENTARIES', 'DOCUMENTARIES'), 
                                                 ('SHORT FILMS', 'SHORT FILMS')])
