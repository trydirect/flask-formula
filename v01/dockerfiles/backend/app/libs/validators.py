from wtforms import ValidationError


class PasswordValidator(object):

    def validate(self, data):
        if isinstance(data, str):
            return any(ch.isdigit() for ch in data)
        return False

    def __call__(self, form, field):
        if field.data:
            if not self.validate(field.data):
                raise ValidationError(field.gettext(u'Invalid password, pleas enter at least one digit.'))