FROM python:2.7

ENV TZ=America/Mexico_City

WORKDIR /usr/src/app

COPY . .

RUN \
    apt-get update && \
    apt-get upgrade -y && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    pip install --no-cache-dir -r requirements.txt

VOLUME ./files /usr/src/app/files

EXPOSE 8000

CMD ["gunicorn", "demo.wsgi:application", "--bind", "0.0.0.0:8000"]