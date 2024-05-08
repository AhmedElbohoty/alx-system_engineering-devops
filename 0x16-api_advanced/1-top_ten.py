#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit(string): the subreddit name
    """

    if subreddit is None:
        print("None")
        return

    if not isinstance(subreddit, str):
        print("None")
        return

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    user_agent = {
        'User-agent': 'Chrome/100.0.4896.100'}
    params = {'limit': 10}
    allow_redirects = False
    timeout = 5000

    response = get(url, headers=user_agent,
                   params=params, allow_redirects=allow_redirects,
                   timeout=timeout)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get('data').get('children')
        for post in data:
            print(post.get('data').get('title'))

    except Exception:
        print("None")
