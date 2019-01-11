from hashlib import md5
from functools import wraps
from itsdangerous import URLSafeTimedSerializer
from flask import request
from flask import current_app


class ConfigurationException(Exception):
    pass


class _SecurityState(object):
    def __init__(self, serializer, secure_config):
        self.serializer = serializer
        for key, value in secure_config.items():
            setattr(self, key.lower(), value)

    def generate_auth_token(self, user_model):
        return self.serializer.dumps("%s|1" % user_model.get_id)

    def generate_enc_data(self, user_id, data):
        return self.serializer.dumps("%s|%s" % (user_id, data))

    def read_enc_data(self, token_data):
        try:
            user_data = self.serializer.loads(token_data, max_age=self.token_max_age)
            return True, user_data
        except Exception as e:
            return False, '%s: %s' % (e.__class__.__name__, e.message)

    def read_auth_token(self):
        token_data = request.headers.get(self.token_header_key)
        if not token_data:
            return False, 'Token header does not exists (use %s to pass it)' % self.token_header_key
        else:
            try:
                user_data = self.serializer.loads(token_data, max_age=self.token_max_age)
                return True, user_data
            except Exception as e:
                return False, '%s: %s' % (e.__class__.__name__, e.message)


class Security(object):
    def __init__(self, app=None, **kwargs):
        self.app = app

        if app is not None:
            self._state = self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        try:
            secure_config = {
                'key': app.config['SECRET_KEY'],
                'salt': app.config['SECURITY_PASSWORD_SALT'],
                'token_max_age': app.config['SECURITY_TOKEN_MAX_AGE'],
                'token_header_key': app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER']
            }
        except:
            raise ConfigurationException('Configuration key for authentication system is missing')

        state = _SecurityState(
            serializer=URLSafeTimedSerializer(secret_key=secure_config['key'],
                                              salt=secure_config['salt']),
            secure_config=secure_config)

        app.security = state
        return state


def login_user(user_model):
    """should do much more functions, but now, it returns the auth token at least"""
    if not hasattr(user_model, 'get_id') :
        raise Exception("User model should implement `get_id` and `get_role` methods")
    return current_app.security.generate_auth_token(user_model)


def __has_rights():
    """call after attribute `user_role` was set for `request` object"""
    if request.user_role not in current_app.config['ACL'].get('%s|%s' % (request.endpoint, request.method.lower()), []):
        return False
    return True


def auth_token_required(fn):
    """place this decorator only before `marshal_with` decorator (flask_restful.marshal_with)"""

    @wraps(fn)
    def decorated(*args, **kwargs):
        token_resp = current_app.security.read_auth_token()
        if token_resp[0]:
            # todo: save some data about user in cache
            token_data = token_resp[1].split('|')
            request.user_id = token_data[0]
            
            return fn(*args, **kwargs)
        else:
            return ({'success': False,
                     'errors': {'global_error': token_resp[1]}},
                    401)

    return decorated


def auth_token_not_required(fn):
    """place this decorator only before `marshal_with` decorator (flask_restful.marshal_with)"""

    @wraps(fn)
    def decorated(*args, **kwargs):
        token_resp = current_app.security.read_auth_token()
        if token_resp[0]:
            return ({'success': False,
                     'errors': {'global_error': 'This resource should be accessed without user auth token'}},
                    401)
        else:
            return fn(*args, **kwargs)

    return decorated


def password_encrypt(password_string):
    # todo: password encryption vulnerability
    return md5(password_string.encode('utf-8')).hexdigest()
