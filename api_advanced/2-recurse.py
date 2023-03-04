#!/usr/bin/python3
"""Module for recurse function"""
import requests


def recurse(subreddit, after='', hot_list=[], page_count=0):
    """Function that queries the Reddit API."""
    url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, parmas=params)
    params = {'limit': 100, 'after': after}

    if response.status_code == 200:
        json_data = response.json()

        for child in json_data.get('data').get('children'):
            title = child.get('data').get('title')
            hot_list.append(title)

        after = json_data.get('data').get('after')
        if after is not None:

            page_count += 1
            return recurse(subreddit, after=after,
                           hot_list=hot_list, page_count=page_count)
        else:
            return hot_list

    else:
        return None


if __name__ == '__main__':
    print(recurse("zerowastecz"))
