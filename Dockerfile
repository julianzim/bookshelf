FROM python:3.12.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache curl && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod -R 777 /app
