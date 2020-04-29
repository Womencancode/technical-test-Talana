# Pulling an official base image
FROM python:3.7-alpine

# Declaring maintainer
MAINTAINER Ignacio

# Setting environment variables
ENV PYTHONUNBUFFERED 1

# Installing dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client git
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setting Up directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

# Adding and run as non-root user
RUN adduser -D user
USER user
