#!/usr/bin/python3
"""
import the modules
"""
import json
import requests


def top_ten(subreddit):
    """
    set the custom User-Agent header
    """
    headers = {'User-Agent': 'Google Chrome Version 114.0.5735.198'}

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
