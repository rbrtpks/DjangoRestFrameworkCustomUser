FROM python:3.8.0-slim

RUN apt-get update && apt-get install gcc -y && apt-get clean
RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
