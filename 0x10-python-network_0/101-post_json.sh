#!/bin/bash
#sends a Json Post request to url json is in file argument 2, url argument 1
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
