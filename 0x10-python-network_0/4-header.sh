#!/bin/bash
#sends custom header with Get request

user_id_header="X-School-User-Id: 98"
curl -s -H "$user_id_header" "$1"
