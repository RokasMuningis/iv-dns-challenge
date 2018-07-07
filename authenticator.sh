#!/bin/bash

DIR="$( cd "$( dirname "$0" )" && pwd )"

source "$DIR/yaml.sh"
create_variables "$DIR/config.yml"
API_URL="https://api.iv.lt/json.php"
COMMAND="domain_zone"
PAYLOAD="$domain_zone,{\"name\":\"_acme-challenge\",\"type\":\"TXT\",\"value\":\"\\\"$CERTBOT_VALIDATION\\\"\"}]"
HTTP_RESPONSE=$(curl --data-urlencode "nick=$username" --data-urlencode "password=$password" --data-urlencode "command=$COMMAND" --data-urlencode "id=$domain_id" --data-urlencode "zone=$PAYLOAD" -g --write-out "HTTPSTATUS:%{http_code}" -X POST "$API_URL")
HTTP_BODY=$(echo $HTTP_RESPONSE | sed -e 's/HTTPSTATUS\:.*//g')