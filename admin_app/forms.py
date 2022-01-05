from wtforms.form import Form
from wtforms.fields.simple import StringField
from wtforms.validators import ValidationError, InputRequired
from admin_app.UploadField import FileUploadField
import settings

allowed_ext = {'mp4'}

def IntegerValidator(form, field):
    try:
        int(field.data)
    except:
        raise ValidationError('Field must an integer')


class ProjectForm(Form):
    order_num = StringField('Order number', validators=[InputRequired(), IntegerValidator])
    name = StringField('Name', validators=[InputRequired()])
    video_url = FileUploadField(
                                'Video', 
                                base_path=settings.content_path, 
                                allowed_extensions = allowed_ext,
                                validators=[InputRequired()])
    slug = StringField('Slug', validators=[InputRequired()])