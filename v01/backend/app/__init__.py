from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_redis import FlaskRedis
from app.libs.app import Api
from app.libs.auth import Security

app = Flask(__name__)
app.config.from_object('app.config.config.Config')
api = Api(app)
db = SQLAlchemy(app)
security = Security(app)
mail = Mail(app)
redis_store = FlaskRedis(app, decode_responses=True)

from app.apps.user import views as user
from app.apps.hello import views as hello

# ---- endpoints ---- #
api.add_resource(user.Auth, '/api/v1/auth', endpoint='auth')
api.add_resource(hello.HelloWorld, '/api/v1/hello', endpoint='hello.test')
