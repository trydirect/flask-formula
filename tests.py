#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import docker
import requests

client = docker.from_env()


# Testing Symfony build

time.sleep(20)  # we expect all containers are up and running in 20 secs

# NGINX
nginx = client.containers.get('nginx')
nginx_cfg = nginx.exec_run("/usr/sbin/nginx -T")
assert nginx.status == 'running'
assert 'server_name _;' in nginx_cfg.output.decode()
assert "error_log /proc/self/fd/2" in nginx_cfg.output.decode()
assert "location = /.well-known/acme-challenge/" in nginx_cfg.output.decode()
assert 'HTTP/1.1" 500' not in nginx.logs()

# test restart
nginx.restart()
time.sleep(3)
assert nginx.status == 'running'

# Kibana
kibana = client.containers.get('kibana')
assert kibana.status == 'running'
response = requests.get("http://127.0.0.1:5601")
assert response.status_code == 200
assert "var hashRoute = '/app/kibana'" in response.text
assert '"statusCode":404,"req":{"url":"/elasticsearch/logstash-' not in kibana.logs()

# Logstash
logstash = client.containers.get('logstash')
assert logstash.status == 'running'
print(logstash.logs())
# assert 'Successfully started Logstash API endpoint {:port=>9600}' in logstash.logs()
# assert 'Pipeline main started' in logstash.logs()

# Elasticsearch
elastic = client.containers.get('elasticsearch')
assert elastic.status == 'running'
response = requests.get("http://127.0.0.1:9200")
assert response.status_code == 200
assert '"number" : "5.4.3"' in response.text
assert ' bound_addresses {0.0.0.0:9200}' in elastic.logs()

web = client.containers.get('web')
assert web.status == 'running'

redis = client.containers.get('redis')
assert redis.status == 'running'
redis_cli = redis.exec_run("redis-cli ping")
assert 'PONG' in redis_cli.output.decode()
redis_log = redis.logs()
assert "Ready to accept connections" in redis_log.decode()

db = client.containers.get('db')
assert db.status == 'running'
cnf = db.exec_run('psql -U symfony -h 127.0.0.1 -p 5432 -c "select 1"')
print(cnf.output.decode())
log = db.logs()
# assert "Ready to accept connections" in log.decode()

mq = client.containers.get('mq')
assert mq.status == 'running'
logs = mq.logs()
assert 'Server startup complete; 3 plugins started' in logs.decode()

for c in client.containers.list():
    assert c.status == 'running'

#response = requests.get("http://127.0.0.1:9000")
#assert response.status_code == 200

