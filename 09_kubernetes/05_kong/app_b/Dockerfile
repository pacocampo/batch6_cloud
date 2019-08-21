FROM python:3.7

ENV FLASK_APP=app.py

RUN apt-get update -y

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "application.py"]