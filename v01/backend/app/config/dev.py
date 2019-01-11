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

    RABBITMQ_HOST = 'mq'
    RABBITMQ_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
    RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_DEFAULT_PASS')