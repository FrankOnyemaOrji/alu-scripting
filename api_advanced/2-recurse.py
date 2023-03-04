#!/usr/bin/python3
"""Module for recurse function"""
import requests


def recurse(subreddit, after='', hot_list=[], page_count=0):
    """Function that queries the Reddit API."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10" \
        .format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    params = {'limit': 100, 'after': after}

    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data:
            hot_list.append(post.get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is not None:
            return recurse(subreddit, after,
                           hot_list, page_count + 1)
        return hot_list
    else:
        return None
