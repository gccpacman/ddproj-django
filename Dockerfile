FROM docker.pkg.github.com/gccpacman/dockerfiles/python:latest

WORKDIR /data

ADD . /data/

RUN  pip install -r requirements.txt