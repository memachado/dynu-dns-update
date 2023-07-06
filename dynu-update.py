import json

config = open('./confi.json', 'r')
conteudo = config.read()

y = json.loads(conteudo)

print(y["endpoint"])
