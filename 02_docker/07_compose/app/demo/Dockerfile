FROM python:3.6

ENV TZ=America/Mexico_City

RUN \
    apt-get update && \
    apt-get upgrade -y && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
