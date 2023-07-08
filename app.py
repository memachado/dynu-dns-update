import json
from requests import get
import dns.resolver

config_text = open('./config.json', 'r').read()
config = json.loads(config_text)

public_ip = get('https://api.ipify.org?format=json').json()['ip']
print('public_ip', public_ip)

def check_dns():
    for host in config['hosts']:
        for alias in config['hosts'][host]['aliases']:
            current_alias_ip = public_resolver(alias+"."+host)
            print(alias+"."+host, current_alias_ip[0].address)
            if public_ip != current_alias_ip[0].address:
                print("tem que atualizar...")
                update_dns_alias(host, alias)
            else: 
                print("não tem que atualizar")
                
def public_resolver(host_url):
    aresolver = dns.resolver.Resolver()
    aresolver.nameservers = ["8.8.8.8"]
    return list(aresolver.resolve(host_url, "A"))

def update_dns_alias(host_name, alias_name):
    url = config['endpoint'].replace("_HOSTNAME_", host_name)
    url = url.replace("_ALIAS_", alias_name)
    url = url.replace("_CURRENT_IP_", public_ip)

    response = get(url, auth=(config['credentials']['user'], config['credentials']['pass']))
    print(response)

if __name__ == "__main__":
    check_dns()

