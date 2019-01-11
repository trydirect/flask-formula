from copy import copy
from flask_wtf import FlaskForm
from wtforms import fields as fl, validators as vl


class BaseForm(FlaskForm):

    def set_foreign_errors(self, error_dict):
        for error_field in error_dict:
            setattr(getattr(self, error_field), 'errors', error_dict[error_field])

    @property
    def str_form_errors(self):
        new_dict = {}
        for err in self.errors:
            try:
                new_dict[err] = ", ".join(self.errors[err])
            except TypeError:
                new_dict[err] = str(self.errors[err])
        return new_dict

    @property
    def prepared_data(self):
        data = {}
        for field in self.data:
            if self.data[field] not in ['None', None]:
                data[field] = self.data[field]
        return data


class PageForm(BaseForm):
    page = fl.IntegerField(default=1, validators=[vl.NumberRange(min=1)])
    per_page = fl.IntegerField(default=10, validators=[vl.NumberRange(max=100)])