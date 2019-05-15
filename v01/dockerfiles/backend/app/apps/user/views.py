from time import time
import string
import random
from datetime import datetime, timedelta
from hashlib import md5
from uuid import uuid4
from flask import render_template, current_app, request
from flask_mail import Message #, Mail
from app.libs.controllers import Resource
from app.libs.controllers import marshal_with
from app.libs.auth import login_user, auth_token_required, auth_token_not_required, password_encrypt
from app import db
from app.apps.user import forms
from .resource_schemas import CustomerSchema
from .models import Users


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y-2)).join(random.choice(string.digits) for x in range(2))


class Auth(Resource):

    @marshal_with(CustomerSchema, envelope='response')  #todo: marshal_with only at status 200/
    def post(self):
        """
        @api {post} /api/v1/auth/ Authenticate
        @apiVersion 0.1.0
        @apiName auth
        @apiGroup auth
        @apiDescription Authenticate a customer and returns a token that should be used in header
                        as `Authentication-Token`
        @apiParam {String}      email        Customer's email.
        @apiParam {String}      password      Customer's password.
        @apiSuccessExample Success-Response:
            HTTP/1.1 200 OK
            {
                "success": true,
                "response":
                    {
                        "auth_token": "token_string_goes_here"
                    }
            }
        @apiErrorExample Error-Response:
            HTTP/1.1 401
            {
              "errors": {
                "global_error": {
                  "code": 186976853,
                  "message": "Incorrect credentials"
                }
              },
              "success": false
            }
        @apiErrorExample Error-Response:
            HTTP/1.1 401
            {
              "errors": {
                "fields": {
                  "password": {
                    "code": 663292517,
                    "message": "This field is required."
                  }
                },
                "global_error": {
                  "code": 805898986,
                  "message": "Fields validation error"
                }
              },
              "success": false
            }
        """
        form = forms.LoginForm()
        if form.validate():
            user_data = form.get_user()
            if user_data:
                token = login_user(user_data)
                user_data.auth_token = token
                return user_data.serialize()
            else:
                return {'success': False, 'errors': {'global_error': 'Incorrect credentials'}}, 401
        return {'success': False, 'errors': form.str_form_errors}, 401
