#!/bin/bash

# Get current dir for includes/requires
DIR="$( cd "$( dirname "$0" )" && pwd )"

# Load yaml parse lib
source "$DIR/yaml.sh"

# Load config
create_variables "$DIR/config.yml"

# Create payload
PAYLOAD="$domain_zone,{\"name\":\"_acme-challenge\",\"type\":\"TXT\",\"value\":\"\\\"$CERTBOT_VALIDATION\\\"\"}]"

# Send request to API
curl --data-urlencode "nick=$username" --data-urlencode "password=$password" --data-urlencode "command=domain_zone" --data-urlencode "id=$domain_id" --data-urlencode "zone=$PAYLOAD" -g -X POST "$api_url"

# Sleep 16 minutes for TTL
sleep 960