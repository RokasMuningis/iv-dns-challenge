#!/usr/bin/env python

import http.client
import urllib.parse
import json
import os

cwd = os.path.abspath(__file__).replace("/run.py", "")

def main():
    with open("%s/%s" % (cwd, "config.json"), 'r') as stream:
        config = json.load(stream)
        api = http.client.HTTPSConnection("api.iv.lt", 443)
        params = urllib.parse.urlencode({
            'nick': config['nick'],
            'password': config['password'],
            'command': 'domain_info',
            'id': config['domain_id']
        })
        api.request("POST", "/json.php", params)
        domain_info = api.getresponse()

if __name__ == "__main__":
    main()
