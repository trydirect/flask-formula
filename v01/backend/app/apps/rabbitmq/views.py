from app.libs.controllers import Resource
import pika
from flask import current_app


class RabbitMQSent(Resource):
        """

        @api {get} /api/v1/rabbit/send RabbitMQ
        @apiVersion 0.1.0
        @apiName rabbit
        @apiGroup rabbit
        @apiDescription Checks connecting to RabbitMQ and then create queue named `hello`
        @apiSuccessExample Success-Response:
            HTTP/1.1 200 OK
            {
                "success": true,
                "response": "Created queue name `hello` and saved value"
            }
        @apiError (500 Internal Server Error) InternalServerError The server encountered an internal error
        @apiError ( 404 Not Found) Not Found

        """
        def get(self):
            port = 5672
            credentials = pika.PlainCredentials("guest", "guest")
            params = pika.ConnectionParameters(host="mq", port=port, credentials=credentials)
            connection = pika.BlockingConnection(params)
            channel = connection.channel()

            channel.queue_declare(queue='hello')

            channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  body='Hello World!')

            connection.close()
            return {
                'success': True,
                'response': 'Created queue name `hello` and saved value'
            }


class RabbitMQReceive(Resource):
    def get(self):
        """

        @api {get} /api/v1/rabbit/send RabbitMQ
        @apiVersion 0.1.0
        @apiName rabbit
        @apiGroup rabbit
        @apiDescription Connecting to RabbitMQ and then create queue named `hello`
        @apiSuccessExample Success-Response:
            HTTP/1.1 200 OK
            {
                 "success": true,
                 "response": "We have got value from queue `hello`"
            }
        @apiError (500 Internal Server Error) InternalServerError The server encountered an internal error
        @apiError ( 404 Not Found) Not Found

                """
        port = 5672

        credentials = pika.PlainCredentials("guest", "guest")
        params = pika.ConnectionParameters(host="mq", port=port, credentials=credentials)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        def callback(ch, meimportthod, properties, body):
            return "Received %r" % body

        channel.basic_consume(
            callback,
            queue='hello',
            no_ack=True
        )

        print('Waiting for messages.')
        channel.start_consuming()
        return {
            'success': True,
            'response': 'We have got value from queue `hello`'
        }