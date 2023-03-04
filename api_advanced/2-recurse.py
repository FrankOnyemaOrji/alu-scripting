#!/usr/bin/python3
"""Module for recurse function"""
import requests


def recurse(subreddit, after='', hot_list=[], page_count=0):
    """Function that queries the Reddit API."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10" \
        .format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, parmas=params)
    params = {'limit': 100, 'after': after}

    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for post in data:
            hot_list.append(post.get('data').get('title'))
        after = data.get('after')
        if after is not None:
            page_count += 1
            recurse(subreddit, after, hot_list, page_count)
        else:
            return hot_list
    else:
        return None

if __name__ == "__main__":
    print(recurse("programming is logical"))

    
