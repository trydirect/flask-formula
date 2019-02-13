from app.libs.controllers import Resource
from app.libs.controllers import marshal_with
from app.libs.auth import login_user, auth_token_required, auth_token_not_required, password_encrypt
from .resource_schemas import DemoSchema
from app import mail, app, redis_store
from flask_mail import Message, Mail
import redis


class RedisTest(Resource):
    def get(self):
        """

        @api {get} /api/v1/redis Test Redis
        @apiVersion 0.1.0
        @apiName redis
        @apiGroup redis
        @apiDescription Checks connecting to Redis and create key with value
        @apiSuccessExample Success-Response:
            HTTP/1.1 200 OK
            {
                "success": True,
                "response": "Connected!"
            }
        @apiError (500 Internal Server Error) InternalServerError The server encountered an internal error
        @apiError ( 404 Not Found) Not Found
        @apiErrorExample Error-Response:
            HTTP/1.1 400
            {
                "success": false,
                "response": "Something went wrong!"
            }
        """
        try:
            conn = redis.Redis(host=app.config.get('REDIS_HOST'),
                               port=app.config.get('REDIS_PORT'))
            conn.ping()
            conn.set('test', 'Hello World!')
            return {
                'success': True,
                'response': 'Connected!'
            }, 200
        except Exception as e:
            return {
                'success': False,
                'response': 'Something went wrong!'
            }, 400


class HelloWorld(Resource):

    @marshal_with(DemoSchema, envelope='result')
    @auth_token_required
    def post(self):
        """
        @api {post} /api/v1/hello/positive_rate/ Predict positive rate
        @apiVersion 0.1.0
        @apiName List
        @apiGroup Predict
        @apiDescription Returns the predicted positive rate
        @apiSuccessExample Success-Response:
            HTTP/1.1 200 OK
            {
                "success": true,
                "result":{
                    "number": 2389
                }
            }
        @apiErrorExample Error-Response:
            HTTP/1.1 200
            {
                "success": false,
                "errors":{
                    "global_error":{
                        "code": 3066431594,
                        "message": "Not found"
                    }
                }
            }

        """
        number = 101

        return {'number': number}

    def get(self):
        """

        @api {get} /api/v1/hello/ Hello
        @apiVersion 0.1.0
        @apiName GetHello
        @apiGroup Hello
        @apiDescription Returns simple string `Hello World!`
        @apiSuccessExample Success-Response:
            HTTP/1.1 200 OK
            {
                "Hello World!"
            }
        @apiError (500 Internal Server Error) InternalServerError The server encountered an internal error
        @apiError ( 404 Not Found) Not Found

        """
        return "Hello World"


class MailTest(Resource):
    def get(self):
        """

        @api {get} /api/v1/mail Send of Mail
        @apiVersion 0.1.0
        @apiName mail
        @apiGroup mail
        @apiDescription Checking was send messages or not
        @apiSuccessExample Success-Response:
            HTTP/1.1 200 OK
            {
                "success": "true",
                "response": "Mail sent!"
            }
        @apiError (500 Internal Server Error) InternalServerError The server encountered an internal error
        @apiError ( 404 Not Found) Not Found
        @apiErrorExample Error-Response:
            HTTP/1.1 400
            {
                "success": false,
                "response": "Something went wrong!"
            }

        """
        message = 'Hello'
        try:
            msg = Message(
                'Test',
                body=message,
                sender=app.config.get('MAIL_DEFAULT_SENDER'),
                recipients=["test@gmail.com"]
            )
            mail.send(msg)
            return {
                'success': True,
                'response': 'Mail sent!'
            }, 200
        except Exception as e:
            return {
               'success': False,
               'response': "Something went wrong!"
            }, 400