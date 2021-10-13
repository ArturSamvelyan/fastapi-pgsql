FROM python:3.8

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ../../web/ .
COPY ../requirements.txt /usr/src/app/requirements.txt

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential gcc libsndfile1 \
    && pip3 install --upgrade pip setuptools wheel \
    && pip3 install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /usr/src/app