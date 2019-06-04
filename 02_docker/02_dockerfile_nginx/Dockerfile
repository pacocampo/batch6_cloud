FROM ubuntu:18.04

RUN apt-get update -y \
    && apt-get install nginx -y

COPY ./nginx.conf /etc/nginx/conf.d

EXPOSE 8000