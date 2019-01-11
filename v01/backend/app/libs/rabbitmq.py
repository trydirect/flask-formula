import pika
import json
import logging
import uuid


class RpcClient(object):

    def __init__(self):
        from flask import current_app

        rabbit_host = current_app.config.get('RABBITMQ_HOST')
        rabbit_user = current_app.config.get('RABBITMQ_USER')
        rabbit_pwd = current_app.config.get('RABBITMQ_PASSWORD')

        credentials = pika.PlainCredentials(rabbit_user, rabbit_pwd)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, credentials=credentials))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, predict_data):

        data = json.dumps(predict_data)
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=data)
        while self.response is None:
            self.connection.process_data_events()
        return self.response
