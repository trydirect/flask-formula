import os
import datetime
from .acl import accesses


class DefaultConfig(object):
    DEBUG = True
    TESTING = True
    APPLICATION_ROOT = '/api/v1/'
    WTF_CSRF_ENABLED = False
    DOMAIN_NAME = os.environ.get('DOMAIN_NAME')
    API_DOMAIN_NAME = os.environ.get('API_DOMAIN_NAME')
    BRAND_NAME = os.environ.get('BRAND_NAME')
    PROTOCOL = 'http'

    # required by flask-login
    SECRET_KEY = 'generate-new-secret'

    # required by flask-security
    # todo: use password encryption
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = 'generate-new-secret'
    SECURITY_EMAIL_SENDER = 'app@optimum-web.com'

    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    SECURITY_TOKEN_MAX_AGE = 2592000

    # additional headers
    ACCESS_CONTROL_ALLOW_ORIGIN_HEADER = '*'
    ACCESS_CONTROL_ALLOW_HEADERS = 'X-Requested-With, Content-Type, X-Custom-Header'
    ACCESS_CONTROL_ALLOW_METHODS = 'GET, POST, PUT, PATCH, DELETE'

    # auth validation
    PASSWORD_HISTORY_DIFFERENCE = 4

    # accesses
    ACL = accesses
