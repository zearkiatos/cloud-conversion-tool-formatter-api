FROM python:alpine3.11

COPY . /app/

WORKDIR /app

RUN apk update && apk upgrade
RUN apk add --no-cache build-base
RUN apk add --no-cache g++ jpeg-dev zlib-dev libjpeg make gcc
RUN apk add --no-cache libffi-dev
RUN apk add --no-cache python3-dev  py-pip
RUN apk add --no-cache py-pip py-virtualenv
RUN apk add --no-cache ffmpeg
RUN pip install --upgrade pip setuptools
RUN pip install --upgrade pip
RUN pip install wheel
RUN make install

EXPOSE 8000

ENTRYPOINT ["sh", "./docker/entrypoint.sh"]