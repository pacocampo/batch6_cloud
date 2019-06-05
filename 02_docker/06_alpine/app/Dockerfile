FROM python:3.6-alpine

RUN apk add python3-dev libffi-dev openssl-dev\
    gcc musl-dev \
    jpeg-dev zlib-dev


ENV TZ=America/Mexico_City

WORKDIR /usr/src/app

COPY ./demo .

RUN pip install -r requirements.txt && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    apk del .build-deps

CMD ["gunicorn", "demo.wsgi:application", "--bind", "0.0.0.0:8000"]