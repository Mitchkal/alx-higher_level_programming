#!/usr/bin/python3
"""
module 3-error_code
"""
import urllib.request
from urllib.error import URLError
import sys


def display_error_code(url):
    """
    didplays body of response or error code
    """

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)

    except URLError as e:
        if hasattr(e, 'code'):
            print("Error code: {}".format(e.code))


if __name__ == "__main__":
    url = sys.argv[1]
    display_error_code(url)
