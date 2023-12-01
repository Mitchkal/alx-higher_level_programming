#!/usr/bin/python3
"""module 0-hbtn_status
"""
import urllib.request


def fetch():
    """
    feches a https link using urllib
    """

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        content = response.read()

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf-8'))


if __name__ == "__main__":
    fetch()
