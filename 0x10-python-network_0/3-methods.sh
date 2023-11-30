#!/bin/bash
#displays http methods accepted by server

curl -sI "$1" | grep -i "Allow:" | cut -f2- -d' '
