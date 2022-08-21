FROM python:3.9-alpine
WORKDIR /backend

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
COPY  . .