# Define a imagem base
FROM python:3.8

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte do projeto para o diretório de trabalho
COPY . .

# Define o comando para iniciar a aplicação
CMD [ "python", "app.py" ]
