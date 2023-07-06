import json

config = open('./config.json', 'r')
conteudo = config.read()

y = json.loads(conteudo)

print(y["endpoint"])
