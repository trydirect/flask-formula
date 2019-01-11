from flask import request, abort
from app.libs.controllers import Resource
from app.libs.controllers import marshal_with
from app.libs.rabbitmq import RpcClient
from app.libs.auth import login_user, auth_token_required, auth_token_not_required, password_encrypt
from .resource_schemas import DemoSchema
import logging
import json

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
        return "Hello World"
