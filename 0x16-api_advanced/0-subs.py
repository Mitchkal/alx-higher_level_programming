#!/usr/bin/python3
"""module subs"""
import requests


def number_of_subscribers(subreddit):
    """querries Reddit API abd returns no of subsribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()['data']
        return (data['subscribers'])
    except Exception as e:
        return (0)
