# Define a imagem base
FROM python:3.11.4-alpine3.17

COPY . .
COPY config.json config.json

RUN pip install --no-cache-dir -r requirements.txt

RUN crontab crontab

CMD ["crond", "-f"]
