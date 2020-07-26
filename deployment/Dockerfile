FROM python:3.8-slim
RUN apt-get update && apt-get install -y \
  net-tools iputils-ping curl wget vim-tiny python-dev nginx libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -y autoremove && \
    apt-get -y clean

ENV PYTHONDONTWRITEBYTECORE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt
