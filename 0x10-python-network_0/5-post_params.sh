#!/bin/bash
#sends a post request with variables in body and gets response

email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -X POST -d "email=$email&subject=$subject" "$1"
