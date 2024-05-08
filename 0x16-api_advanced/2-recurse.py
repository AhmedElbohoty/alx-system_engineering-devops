#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Write a recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function return None.
    """

    if subreddit is None:
        return 0

    if not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    allow_redirects = False
    timeout = 5000

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=allow_redirects, timeout=timeout)

    if response.status_code != 200:
        return None

    data = response.json().get('data')

    if data is None:
        return None

    children = data.get('children')
    if not children:
        return None

    for child in children:
        title = child.get('data', {}).get('title')
        if title:
            hot_list.append(title)

    after = data.get('after')

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
