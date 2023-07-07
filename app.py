import json
from requests import get, status_codes, codes, utils, exceptions
import socket

config = open('./config.json', 'r')
conteudo = config.read()

y = json.loads(conteudo)

print(y["endpoint"])


addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('yahoo.com')
print(addr1, addr2)

response = get('https://api.ipify.org?format=json')
data = response.json()
public_ip = data['ip']
print(public_ip)