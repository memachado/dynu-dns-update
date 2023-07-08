import json
import socket
from requests import get, status_codes, codes, utils, exceptions
import dns.edns
import dns.message
import dns.query
import dns.resolver


def update_dns():

    config_text = open('./config.json', 'r').read()
    config = json.loads(config_text)

    public_ip = get('https://api.ipify.org?format=json').json()['ip']
    print('public_ip', public_ip)
    
    for host in config['hosts']:
        for alias in config['hosts'][host]['aliases']:
            current_alias_ip = public_resolver(alias+"."+host)
            print(alias, current_alias_ip[0].address)
            if public_ip != current_alias_ip[0].address:
                print("tem que atualizar")
            else: 
                print("não tem que atualizar")
                
def public_resolver(host_url):
    aresolver = dns.resolver.Resolver()
    aresolver.nameservers = ["8.8.8.8"]
    return list(aresolver.resolve(host_url, "A"))

if __name__ == "__main__":
    update_dns()

