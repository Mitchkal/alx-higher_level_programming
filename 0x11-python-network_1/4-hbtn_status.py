#!/usr/bin/python3
"""
module 4-hbtn_status
"""
import requests


def fetch_request(url):
    """
    fetches  a url and displays the response
    """

    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_request(url)
