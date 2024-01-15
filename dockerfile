FROM python:3.11.4-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update


RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN pip install django djangorestframework

COPY . /app

ENTRYPOINT [ "gunicorn", "core.wsgi"]