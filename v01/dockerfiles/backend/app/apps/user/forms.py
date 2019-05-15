from datetime import datetime, timedelta
from flask import request, current_app
from app.libs.auth import password_encrypt
from app.libs.validators import PasswordValidator
from app.libs.forms import BaseForm
from app import db
from wtforms import fields as fl, validators as vl
from .models import Users

class LoginForm(BaseForm):

    email = fl.StringField(validators=[vl.DataRequired(), vl.Email()])
    password = fl.PasswordField(validators=[vl.DataRequired(), vl.length(max=32, min=7), PasswordValidator()])

    def get_user(self):
        """call only after calling validate"""
        c_info = Users.query.filter_by(
            email=self.data.get('email', ''),
            password=password_encrypt(self.data.get('password', ''))).first()
        if not c_info:
            return False
        return c_info
