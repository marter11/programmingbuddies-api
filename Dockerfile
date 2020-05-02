FROM python:3.7-alpine

WORKDIR /pb_api
COPY . /pb_api

# This ugly code is here because we need to install gcc and other dependencies to compile a pip package (`cffi` and `cryptography` IIRC)
# Alpine Linux has no `apt` :( you have to use their package manager called `apk`
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev python3-dev \
     && pip install pipenv \
     && pipenv install --system \
     && apk del .build-deps gcc musl-dev

CMD python src/runserver.py
