#!/usr/bin/python3
"""
module 10-github
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def basic_authenticate(user, password):
    """
    performs basic github authentication
    prits user id from github
    """

    basic = HTTPBasicAuth(user, password)
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=basic)

    print(response.json().get('id'))


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    basic_authenticate(user, password)
