"""
dev environment configuration
"""
from app.config import DefaultConfig
import os


class Config(DefaultConfig):
    API_DOMAIN_NAME = 'auto.optimum-web.com'
    DOMAIN_NAME = 'auto.optimum-web.com'
    PROTOCOL = 'http'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{passw}@{host}/{name}'.format(
        user=os.environ.get('POSTGRES_USER'),
        passw=os.environ.get('POSTGRES_PASSWORD'),
        name=os.environ.get('POSTGRES_DB'),
        host=os.environ.get('POSTGRES_HOST'),
    )

    RABBITMQ_DEFAULT_VHOST = os.environ.get('MQ_SERVER_COMMUNICATE')
    RABBITMQ_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
    RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_DEFAULT_PASS')

    REDIS_HOST = 'redis'
    REDIS_PORT = os.environ.get('REDIS_PORT')
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
    REDIS_URL = "redis://:{password}@{host}:{port}/0".format(
        password=REDIS_PASSWORD,
        host=REDIS_HOST,
        port=REDIS_PORT
    )

    MAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
    MAIL_SERVER = os.environ.get('EMAIL_HOST')
    MAIL_PORT = os.environ.get('EMAIL_PORT')
    MAIL_USERNAME = os.environ.get('EMAIL_HOST_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('DEFAULT_FROM_EMAIL')
