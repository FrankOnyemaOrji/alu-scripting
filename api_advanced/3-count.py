#!/usr/bin/python3
"""Module for count_words function"""
import requests
import json


def count_words(subreddit, word_list, after='', hot_list=[]):
    """Function that queries the Reddit API."""
    if after == '':
        hot_list = [] * len(word_list)
    url = "https://www.reddit.com/r/{}/hot.json?limit=100" \
        .format(subreddit)
    request = requests.get(url, params={'after': after},
                           allow_redirects=False,
                           headers={'User-Agent': 'My User'})

    if request.status_code == 200:
        data = request.json().get('data').get('children')
        for post in data:
            hot_list.append(post.get('data').get('title'))
        after = request.json().get('data').get('after')
        if after is not None:
            return count_words(subreddit, word_list, after, hot_list)
        else:
            for i in range(len(word_list)):
                word_list[i] = word_list[i].lower()
            for i in range(len(hot_list)):
                hot_list[i] = hot_list[i].lower()
            for i in range(len(word_list)):
                hot_list[i] = hot_list[i].split()
            for i in range(len(word_list)):
                hot_list[i] = hot_list[i].count(word_list[i])
            for i in range(len(word_list)):
                print(word_list[i], hot_list[i])
