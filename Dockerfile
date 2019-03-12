FROM node:9-alpine

RUN apk add --no-cache python python-dev python3 python3-dev \
    linux-headers build-base bash git ca-certificates && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

RUN apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone

ENV BUILD_PACKAGES postgresql-dev postgresql-client gettext 

RUN apk update
RUN apk add libffi-dev
RUN apk add --update --no-cache $BUILD_PACKAGES
RUN mkdir -p /var/labhacker/audiencias

ADD . /var/labhacker/audiencias
WORKDIR /var/labhacker/audiencias

RUN pip3 install -r requirements.txt psycopg2 gunicorn && \
    rm -r /root/.cache

RUN npm install && \
    npm rebuild node-sass --force

RUN python3 manage.py bower_install --allow-root && \
    python3 manage.py compress --force && \
    python3 manage.py collectstatic --no-input && \
    python3 manage.py compilemessages

#ADD ./config/etc/cron.d/audiencias /etc/cron.d/audiencias
#RUN chmod 0644 /etc/cron.d/audiencias

EXPOSE 8000
