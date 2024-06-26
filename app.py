import json
from requests import get
import dns.resolver
import os
from datetime import datetime


config_text = open((os.path.join(os.path.dirname(__file__),'config.json')), 'r').read()
config = json.loads(config_text)

public_ip = get('https://api.ipify.org?format=json').json()['ip']
print('public_ip', public_ip)

def check_dns():
    for host in config['hosts']:
        try:
            current_alias_ip = public_resolver(host)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if public_ip != current_alias_ip[0].address:
                print(current_time, 'missmatching ip at ' ,host, current_alias_ip[0].address)
                update_dns_alias(host)
        except Exception as e:
            print(host, "not found")
def public_resolver(host_url):
    aresolver = dns.resolver.Resolver()
    aresolver.nameservers = ["8.8.8.8"]
    return list(aresolver.resolve(host_url, "A"))

def update_dns_alias(host_name):
    url = config['endpoint'].replace("_HOSTNAME_", host_name)
    url = url.replace("_CURRENT_IP_", public_ip)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(current_time, 'updating ', host_name)

    response = get(url, auth=(config['credentials']['user'], config['credentials']['pass']))

    print(response)

if __name__ == "__main__":
    check_dns()

