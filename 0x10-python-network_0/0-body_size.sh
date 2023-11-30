#!/bin/bash
#Gets url and prints reponse's body size

curl -sI "$1" | grep -i 'Content-Length:' | cut -f2 -d' '
