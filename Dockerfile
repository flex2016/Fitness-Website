FROM python:2.7-slim
MAINTAINER Taras Kurilo <taraskurilo@gmail.com>

ENV INSTALL_PATH /fitness
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "fitness.app:create_app()"
