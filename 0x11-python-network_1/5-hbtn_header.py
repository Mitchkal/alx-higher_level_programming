#!/usr/bin/python3
"""
module 5-hbtn_header
"""
import requests
import sys


def header_value(url):
    response = requests.get(url)
    _id = response.headers.get('X-Request-Id')
    print("{}".format(_id))


if __name__ == "__main__":
    url = sys.argv[1]
    header_value(url)
