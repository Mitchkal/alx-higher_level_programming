#!/bin/bash
#takes URL, ends request to it, and displays size of body response


url=$1
response=$(curl -sI "$url")

content_length=$(echo "$response" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r\n')

echo $content_length
