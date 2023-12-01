#!/usr/bin/python3
"""
module 1-hbtn_header.py
"""

import sys
import urllib.request


def send_request(url):

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        _id = response.info().get('X-Request-Id')
        print("{}".format(_id))


if __name__ == "__main__":
    url = sys.argv[1]
    send_request(url)
