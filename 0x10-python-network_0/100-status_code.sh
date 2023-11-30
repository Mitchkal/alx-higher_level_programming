#!/bin/bash
#displays the status code of request

curl -o/dev/null -w'%{http_code}' -sLI "$1"
