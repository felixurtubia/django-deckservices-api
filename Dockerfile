FROM python:3.7-alpine
MAINTAINER Felix Urtubia Carrasco

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add libpq
RUN apk add --virtual .build-deps gcc python-dev musl-dev postgresql-dev


COPY ./requirements.txt /requirements.txt
#RUN apk add python-dev
RUN pip install -r /requirements.txt

WORKDIR /app

COPY ./app /app

RUN celery multi start w1 -A app -l info -Q celery, decks


RUN adduser -D user
USER user


