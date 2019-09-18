FROM python:3.6-alpine

RUN \
    apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

WORKDIR /usr/src/app

COPY app/demo/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["gunicorn", "demo.wsgi:application", "--bind", "0.0.0.0:8000"]