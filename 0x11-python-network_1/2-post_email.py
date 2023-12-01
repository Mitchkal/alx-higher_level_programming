#!/usr/bin/python3
"""
module 2-post_email.py
"""

import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    posts an email to a url and prints the response
    """

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')

        print("Your email is: {}".format(content))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    post_email(url, email)
