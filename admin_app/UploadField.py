import os
import os.path as op

from wtforms import __version__ as wtforms_version
from wtforms import ValidationError, fields


from werkzeug.datastructures import FileStorage

from flask_admin.form.upload import FileUploadInput, namegen_filename
from flask_admin.babel import gettext
from flask_admin._compat import urljoin

try:
    from wtforms.fields.core import _unset_value as unset_value
except ImportError:
    from wtforms.utils import unset_value

class FileUploadField(fields.StringField):
    """
        Customizable file-upload field.
        Saves file to configured path, handles updates and deletions. Inherits from `StringField`,
        resulting filename will be stored as string.
    """
    widget = FileUploadInput()
    def __init__(self, label=None, validators=None,
                 base_path=None, relative_path=None,
                 namegen=None, allowed_extensions=None,
                 permission=0o666, allow_overwrite=True,
                 **kwargs):
        """
            Constructor.
            :param label:
                Display label
            :param validators:
                Validators
            :param base_path:
                Absolute path to the directory which will store files
            :param relative_path:
                Relative path from the directory. Will be prepended to the file name for uploaded files.
                Flask-Admin uses `urlparse.urljoin` to generate resulting filename, so make sure you have
                trailing slash.
            :param namegen:
                Function that will generate filename from the model and uploaded file object.
                Please note, that model is "dirty" model object, before it was committed to database.
                For example::
                    import os.path as op
                    def prefix_name(obj, file_data):
                        parts = op.splitext(file_data.filename)
                        return secure_filename('file-%s%s' % parts)
                    class MyForm(BaseForm):
                        upload = FileUploadField('File', namegen=prefix_name)
            :param allowed_extensions:
                List of allowed extensions. If not provided, will allow any file.
            :param allow_overwrite:
                Whether to overwrite existing files in upload directory. Defaults to `True`.
            .. versionadded:: 1.1.1
                The `allow_overwrite` parameter was added.
        """
        self.base_path = base_path
        self.relative_path = relative_path
        self.namegen = namegen or namegen_filename
        self.allowed_extensions = allowed_extensions
        self.permission = permission
        self._allow_overwrite = allow_overwrite

        self._should_delete = False

        if int(wtforms_version[0]) < 3:
            kwargs.pop('extra_filters', None)

        super(FileUploadField, self).__init__(label, validators, **kwargs)

    def is_file_allowed(self, filename):
        """
            Check if file extension is allowed.
            :param filename:
                File name to check
        """
        if not self.allowed_extensions:
            return True
        return ('.' in filename and
                filename.rsplit('.', 1)[1].lower() in
                map(lambda x: x.lower(), self.allowed_extensions))
    def _is_uploaded_file(self, data):
        return (data and isinstance(data, FileStorage) and data.filename)

    def pre_validate(self, form):
        if self._is_uploaded_file(self.data) and not self.is_file_allowed(self.data.filename):
            raise ValidationError(gettext('Invalid file extension'))
        # Handle overwriting existing content
        if not self._is_uploaded_file(self.data):
            return

    def process(self, formdata, data=unset_value, extra_filters=None):
        if formdata:
            marker = '_%s-delete' % self.name
            if marker in formdata:
                self._should_delete = True

        if int(wtforms_version[0]) < 3:
            return super(FileUploadField, self).process(formdata, data)
        else:
            return super(FileUploadField, self).process(formdata, data, extra_filters)  # noqa

    def process_formdata(self, valuelist):
        if self._should_delete:
            self.data = None
        elif valuelist:
            for data in valuelist:
                if self._is_uploaded_file(data):
                    self.data = data
                    break

    def populate_obj(self, obj, name):
        field = getattr(obj, name, None)
        if field:
            # If field should be deleted, clean it up
            if self._should_delete:
                self._delete_file(field)
                setattr(obj, name, None)
                return
        if self._is_uploaded_file(self.data):
            if field:
                self._delete_file(field)
            filename = self.generate_name(obj, self.data)
            filename = self._save_file(self.data, filename)
            # update filename of FileStorage to our validated name
            self.data.filename = filename
            setattr(obj, name, filename)

    def generate_name(self, obj, file_data):
        filename = self.namegen(obj, file_data)
        if not self.relative_path:
            return filename
        return urljoin(self.relative_path, filename)

    def _get_path(self, filename):
        if not self.base_path:
            raise ValueError('FileUploadField field requires base_path to be set.')
        if callable(self.base_path):
            return op.join(self.base_path(), filename)
        return op.join(self.base_path, filename)

    def _delete_file(self, filename):
        path = self._get_path(filename)
        if op.exists(path):
            os.remove(path)

    def _save_file(self, data, filename):
        path = self._get_path(filename)
        if not op.exists(op.dirname(path)):
            os.makedirs(os.path.dirname(path), self.permission | 0o111)
        if (self._allow_overwrite is False) and os.path.exists(path):
            raise ValueError(gettext('File "%s" already exists.' % path))
        data.save(path)
        return filename