#!/bin/sh

VERSION="1.0.2"
docker-compose build
docker tag build_web:latest optimum/development:flask-formula-$VERSION-s
docker push optimum/development:flask-formula-$VERSION-s
