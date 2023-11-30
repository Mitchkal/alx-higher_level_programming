#!/bin/bash
#sends custom header with Get requesT
curl -s -H "X-School-User-Id: 98" "$1"
