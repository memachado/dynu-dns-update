# Define a imagem base
FROM 3.11.4-alpine3.17

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN crontab crontab

CMD ["crond", "-f"]
