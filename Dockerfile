# ONGAbot
#
# Version latest

FROM tingvarsson/python:latest
MAINTAINER Thomas Ingvarsson <ingvarsson.thomas@gmail.com>

RUN apk add --no-cache --virtual=build-dependencies ca-certificates && \
    pip install --upgrade setuptools && \
    pip install aiogram uvloop ujson && \
    apk del build-dependencies

COPY src /ongabot

ENV API_TOKEN=''

CMD ["/ongabot/ongabot.py"]