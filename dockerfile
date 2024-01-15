FROM python:3.11.4-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update

# install dependencies

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN pip install -r ./requirements.txt

COPY . /app

ENTRYPOINT [ "gunicorn", "core.wsgi"]