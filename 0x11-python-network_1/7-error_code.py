#!/usr/bin/python3
"""module 7-error_code"""
import requests
import sys


def print_error(url):
    """
    prints  errror code for
    url request using module request
    """

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)


if __name__ == "__main__":
    url = sys.argv[1]
    print_error(url)
