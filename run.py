#!/usr/bin/env python

import http.client
import urllib.parse
import json
import os

CWD = os.path.abspath(__file__).replace(__file__, "")
CONFIG_JSON = "config.json"
API_URL = "api.iv.lt"
API_PORT = 443
API_ENDPOINT = "/json.php"
API_METHOD = "POST"
COMMANDS = {
    DOMAIN_INFO: 'domain_info',
    DOMAIN_ZONE: 'domain_zone'
}
SOME_RANDOM_HASH = "SOME_RANDOM_HASH"

def getDomainsInfo(config):
    request = http.client.HTTPSConnection(API_URL, API_PORT)
    payload = urllib.parse.urlencode({
        "nick": config["nick"],
        "password": config["password"],
        "command": COMMANDS.DOMAIN_INFO,
        "id": config["domain_id"]
    })
    request.request(API_METHOD, API_ENDPOINT, payload)
    response = domain_info = api.getresponse()
    handleDomainsInfoResponse(response)

def handleDomainsInfoResponse(response):
    if (domain_info.status == 200):
        response_body = domain_info.read()
        domains = json.load(response_body)
        if (domains["se_zone"])
            postDomainsZone(domains["se_zone"])

def postDomainsZone(domains_zone):
    domains_zone.append({ name: "_acme-challenge", type: "text", value: "\"%s\"" % (SOME_RANDOM_HASH) })
    request = http.client.HTTPSConnection(API_URL, API_PORT)
    payload = urllib.parse.urlencode({
        "nick": config["nick"],
        "password": config["password"],
        "command": COMMANDS.DOMAIN_ZONE,
        "id": config["domain_id"],
        "zone": domains_zone
    })
    request.request(API_METHOD, API_ENDPOINT, payload)


def main():
    with open("%s/%s" % (CWD, CONFIG_JSON), "r") as stream:
        config = json.load(stream)
        getDomainsInfo(config)

if __name__ == "__main__":
    main()
