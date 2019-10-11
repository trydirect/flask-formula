[![Build Status](https://travis-ci.com/trydirect/flask-formula.svg?branch=master)](https://travis-ci.com/trydirect/flask-formula)
![Docker Stars](https://img.shields.io/docker/stars/trydirect/flask-formula.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/trydirect/flask-formula.svg)
![Docker Automated](https://img.shields.io/docker/cloud/automated/trydirect/flask-formula.svg)
![Docker Build](https://img.shields.io/docker/cloud/build/trydirect/flask-formula.svg)
[![Gitter chat](https://badges.gitter.im/trydirect/community.png)](https://gitter.im/try-direct/community)
[<img src="https://img.shields.io/badge/quick%20deploy-%40try.direct-brightgreen.svg">](https://dev.try.direct/server/user/deploy/ImZsYXNrLWZvcm11bGF8NnwxIg.EAoFeA.uX905WE6PHwsURU1_FiOMS0Ar3k/)
	
# Flask Restful API template

Flask Restful API backend template - project generator/development environment.
Can be used by Python developers for quick start on building Restful API on Flask.

## Stack includes

* rabbitmq 
* redis 
* elasticsearch
* logstash
* postgresql
* nginx
* supervisord
* kibana
* apidoc

Extra python libs and validator classes included. 


## Note
Before installing this project, please, make sure you have installed docker and docker-compose

To install docker execute: 
```sh
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sh get-docker.sh
$ pip install docker-compose
```
## Installation

Clone this project into your work directory:

```sh
$ git clone "https://github.com/trydirect/flask-formula.git"
```

Then build it with the following command:
```sh
$ cd flask-formula
$ ./setup.sh
```

Add localdomain to your hosts file Linux, OSX: 

```
echo  "127.0.0.1 localdomain kibana.localdomain" | sudo tee -a /etc/hosts
```

Now, let's check it out
```
$ curl -i localhost/api/v1/hello
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Fri, 24 May 2019 15:33:02 GMT
Content-Type: application/json
Content-Length: 14
Connection: keep-alive
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: X-Requested-With, Content-Type, X-Custom-Header
Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE

"Hello World"
```

Default kibana creds:  
- login: admin   
- password:  admin

| URL | App |
| --- | --- |
| http://localhost | Api doc |
| http://localhost/api/v1/hello | Api hello endpoint |
| http://kibana.localdomain | Kibana dashboard |


## Features

* Full Docker integration
* Docker Compose integration and optimization for local development
* Production ready Python web server using Nginx and uWSGI
* Python Flask backend:
* Nginx plus HTTPS certificate generation with Let's Encrypt 



The final project structure will look like this: 

```
~/flask_formula$ tree
.
├── backend
│   ├── app
│   │   ├── apidoc.json
│   │   ├── apps
│   │   │   ├── hello
│   │   │   │   ├── __init__.py
│   │   │   │   ├── resource_schemas.py
│   │   │   │   └── views.py
│   │   │   ├── __init__.py
│   │   │   ├── rabbitmq
│   │   │   │   ├── __init__.py
│   │   │   │   ├── resource_schemas.py
│   │   │   │   └── views.py
│   │   │   └── user
│   │   │       ├── forms.py
│   │   │       ├── __init__.py
│   │   │       ├── models.py
│   │   │       ├── resource_schemas.py
│   │   │       └── views.py
│   │   ├── config
│   │   │   ├── acl.py
│   │   │   ├── config.py
│   │   │   ├── config.py.dist
│   │   │   ├── dev.py
│   │   │   ├── __init__.py
│   │   │   ├── nginx.conf
│   │   ├── docs
│   │   ├── __init__.py
│   │   ├── libs
│   │   │   ├── app.py
│   │   │   ├── auth.py
│   │   │   ├── controllers.py
│   │   │   ├── forms.py
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── rabbitmq.py
│   │   │   ├── redis_session.py
│   │   │   ├── resource_schemas.py
│   │   │   └── validators.py
│   ├── manage.py
│   ├── migrations
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 9d5e165bc45e_.py
│   │       ├── ce716beab747_.py
│   ├── README.md
│   ├── run.py
│   ├── wsgi.ini
│   └── wsgi.py
├── certs
│   ├── letsencrypt
│   └── ssl
│       ├── cert.pem
│       └── key.pem
├── config.json
├── configs
│   ├── elasticsearch
│   │   └── elasticsearch.yml
│   ├── logstash
│   │   ├── Dockerfile
│   │   ├── logstash.conf
│   │   └── templates
│   │       ├── filebeat.template.json
│   │       ├── packetbeat.template.json
│   │       └── topbeat.template.json
│   ├── nginx
│   │   ├── conf.d
│   │   │   ├── flask_formula.conf
│   │   ├── letsencrypt-conf.d
│   │   │   └── flask_formula.conf
│   │   ├── nginx.conf
│   │   └── ssl-conf.d
│   │       └── flask_formula.conf
│   ├── postgresql
│   │   └── pg_hba.conf
│   ├── supervisord
│   │   ├── flask_formula.conf
│   │   └── nginx.conf
│   ├── systemd
│   │   └── flask_formula.service
│   └── upstart
│       └── flask_formula.sh
├── cron
│   └── root
├── docker-compose.yml
├── docker-firewall.sh
├── elasticsearch
│   └── data
│       └── nodes
│           └── 0
│               ├── node.lock
│               └── _state
│                   └── node-157.st
├── flask_app.tar.gz
├── init-user-db.sh
├── nginx
│   ├── conf.d
│   │   └── flask_formula.conf
│   ├── letsencrypt-conf-d
│   ├── nginx.conf
│   └── ssl-conf.d
├── nginx_original
│   ├── conf.d
│   │   └── flask_formula.conf
│   ├── letsencrypt-conf.d
│   │   └── flask_formula.conf
│   └── ssl-conf.d
│       └── flask_formula.conf
├── scripts
└── supervisord
    ├── flask_formula.conf
    └── nginx.conf
```    

```
$ docker-compose ps

Name                  Command                          State          Ports
------------------------------------------------------------------------------------------------------------------------------
db                    docker-entrypoint.sh postgres    Up (healthy)   5432/tcp
elasticsearch         /docker-entrypoint.sh elas ...   Up             9200/tcp, 9300/tcp
flask_formula_pmm_1   docker-entrypoint.sh postgres    Up             5432/tcp
kibana                /docker-entrypoint.sh kibana     Up             0.0.0.0:5601->5601/tcp
logstash              /docker-entrypoint.sh -e         Up             0.0.0.0:5044->5044/tcp
mq                    docker-entrypoint.sh rabbi ...   Up (healthy)   15671/tcp, 0.0.0.0:21072->15672/tcp, 25672/tcp, 4369/tcp, 5671/tcp, 0.0.0.0:2172->5672/tcp,0.0.0.0:32770->5672/tcp
nginx                 /usr/bin/supervisord -c /e ...   Up             0.0.0.0:443->443/tcp, 0.0.0.0:80->80/tcp
redis                 docker-entrypoint.sh redis ...   Up (healthy)   6379/tcp
web                   /usr/bin/supervisord -c /e ...   Up             0.0.0.0:8000->8000/tcp   
```


## Generate Api Doc
```.env
$ ./scripts/apidoc.sh
```


## Quick deployment to cloud
##### Amazon AWS, Digital Ocean, Hetzner and others
[<img src="https://img.shields.io/badge/quick%20deploy-%40try.direct-brightgreen.svg">](https://dev.try.direct/server/user/deploy/ImZsYXNrLWZvcm11bGF8NnwxIg.EAoFeA.uX905WE6PHwsURU1_FiOMS0Ar3k/)



## Contributing

1. Fork it (https://github.com/trydirect/flask-formula/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request



## Support Development

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2BH8ED2AUU2RL)
