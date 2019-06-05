FROM python:2.7

ENV TZ=America/Mexico_City

RUN \
    apt-get update && \
    apt-get upgrade -y && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

# Trata de descargar lo menos posible de datos
COPY ./venv/bin /usr/local/bin

# Intenta colocar lo más bajo posible el código de tu app
WORKDIR /usr/src/app

COPY ./demo .


CMD ["gunicorn", "demo.wsgi:application", "--bind", "0.0.0.0:8000"]