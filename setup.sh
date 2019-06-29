#!/usr/bin/env bash

printf "admin:`echo "admin" | openssl passwd -stdin`" > ./dockerfiles/configs/nginx/conf.d/.htpasswd
docker-compose up -d
