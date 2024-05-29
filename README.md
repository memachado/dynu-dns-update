# dynu-dns-update

Python script to check current host IPs and update them when needed.

## install

You can either run this on your computer or on a docker

1. Clone this repo
2. Create a `config.json` like this

   ``` json
        {
            "credentials": {
                "user": "",
                "pass": ""
            },
            "endpoint": "https://api.dynu.com/nic/update?hostname=_HOSTNAME_&myip=_CURRENT_IP_",
            "hosts": [
                "somehost.com",
                "anotherhost.com"
            ]
        }
   ```

3. Build the docker `docker build -t dynu-dns .`
4. Run it

## config

You need to provide user and password in the config.json. I prefer to use the sh256 password, as dynu accepts it.

You can choose any url from the reference documentation provided, but the one in the endpoint above works fine.

You can choose how often the cron will execute the script editing the `cronjob` file and rebuilding the container

## reference

https://www.dynu.com/DynamicDNS/IPUpdateClient/cURL
